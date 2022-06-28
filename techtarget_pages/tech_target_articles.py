from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import webbrowser

def get_page(link):

    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs(html, 'html.parser')
    page = soup.find('html').decode()
    '''
    all_urls = dict()
    for tag in soup.find_all('a'):
        all_urls[tag.text] = tag.get('href')
    '''
    file = open(link.split('/')[-1] + '.html', 'w', encoding='utf-8')
    file.write(page);file.flush();file.close()
    webbrowser.open(file.name, 2)

link = input('Enter page link: ')

get_page(link)