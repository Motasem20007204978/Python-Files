from time import sleep
from bs4 import BeautifulSoup as bs
import requests, tempfile, img2pdf
from selenium import webdriver
from io import BytesIO
from PIL import Image


def get_elements(url:str, tag:str, attrs:dict):
    request = requests.get(url)
    soup = bs(request.content, 'html.parser')
    return soup.find_all(tag, attrs=attrs)


exec_script = '''
jQuery(document).ready(function($){
	wp_manga_reporting = false;
	
	$(document).on( 'click', '#btn_flag_chapter', function(evt){
		
		if(confirm(wp_chapter_report.are_you_sure)){
			
			if(!wp_manga_reporting){
				wp_manga_reporting = true;
				
				var volSelect = $('.volume-select');

				var mangaHasVolume = volSelect.length > 0 ? true : false;

				var curVol = mangaHasVolume ? volSelect.val() : 0;

				var	curVolChapSelect = $('.selectpicker_chapter[for="volume-id-' + curVol + '"] .single-chapter-select');
				
				data = {manga: $('#btn_flag_chapter').attr('data-manga'), chapter: curVolChapSelect.val(), action: 'chapter_flag'};
				
				$.ajax({
					type : 'POST',
					url : manga.ajax_url,
					data : data,
					success : function( response ){
						obj = JSON.parse(response);
						wp_manga_reporting = false;
						alert(obj.message);
					},
					error : function(err){
						wp_manga_reporting = false;
						alert(err);
					}
				});
			}
		}
		
		return false;
	});
});
'''


def init_browser(executable_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_prefs = {}
    chrome_prefs["profile.managed_default_content_settings.images"] = 2
    chrome_prefs["profile.default_content_settings.images"] = 2
    # block all downloads
    chrome_prefs["download.download_restrictions"] = 3
    chrome_prefs["download.default_directory"] = tempfile.gettempdir()
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')
    # run chromedriver in silent mode
    chrome_options.add_argument('--log-level=OFF')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
    return browser

def imgs_bytes_as_pdf(list_bytes, pdf_file):
	pdf_images = img2pdf.convert(list_bytes)
	pdf_file.write(pdf_images)
	pdf_file.flush();pdf_file.close()
	print(list_bytes.__len__(), 'images stored as pdf successfully')

def convert_images_to_pdf_file(img_elements:list, pdf_file):
	"""_summary_

	Args:
		img_elements (_type_): img elements from webpage
		pdf_file (_type_): u must create pdf with write bytes mode file as open('path/to/file_name.pdf', 'wb')
		u should use beautifulsoup
	"""	
	listimages = []
	for img in img_elements:

		content = requests.get(img.get('src'))
		sleep(2)

		if content.status_code != 200:

			print('error in image with source', img.get('src'))
			continue

		listimages.append(BytesIO(content.content))
	imgs_bytes_as_pdf(list_bytes=listimages, pdf_file=pdf_file)


def save_imgs_as_pdf(imgs, pdf_file):
	"""_summary_

	Args:
		img_elements (_type_): img elements from webpage
		pdf_file (_type_): u must create pdf with write bytes mode file as open('path/to/file_name.pdf', 'wb')
		u should use selenium
	"""

	list_bytes = []
	for img in imgs:
		png = Image.open(BytesIO(img.screenshot_as_png))
		list_bytes.append(png)
	
	imgs_bytes_as_pdf(list_bytes=list_bytes, pdf_file=pdf_file)
	