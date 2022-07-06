import click, time 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://gmanga.org/')

#access search engine
search_engine = driver.find_element(By.ID, 'quickSearch')

#search for manga u want
search_text = input("Enter name of manga: ")
search_engine.send_keys(search_text)
driver.implicitly_wait(10)
suggested_mangas = driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-quickSearch']/div[1]/ul/li/a")

#suggested mangas according to search
print('suggested mangas:')
for num, link in enumerate(suggested_mangas, start=1):
    name = link.get_attribute('href').split('/')[-1]
    print(f'\n{num}.{name}',)

chosen = click.prompt('\nchoose ', type=click.Choice(list(str(n) for n in range(1, len(suggested_mangas)+1))))
chosen_manga_link = suggested_mangas[int(chosen)-1].get_attribute('href')
chosen_manga_name = chosen_manga_link.split('/')[-1]
driver.get(chosen_manga_link)

time.sleep(30)

#folders for chosen manga
folders = driver.find_elements(By.XPATH, '//div[@id="infiniteVolumes"]/div[2]/div/div/div')
if not folders:
    exit()

folders.reverse()

#choose a folder
print(f'folders for manga {chosen_manga_name}:')
for num, folder in enumerate(folders, start=1):
    print(folder.find_element(By.CLASS_NAME, 'title').text)
chosen = int(click.prompt('\nchoose ', type=click.Choice(list(str(n) for n in range(1, len(folders)+1)))))

#chapters for chosen folder
chapters = folders[chosen-1].find_elements(By.CLASS_NAME, 'chapter-item')
chapters.reverse()

#choose a chapter
print(f'chapters for this folder:')
for num, chapter in enumerate(chapters, start=1):
    print(f'{num}.chapter {chapter.find_element(By.XPATH, "div/div[3]/div").text}')
chosen = int(click.prompt('\nchoose ', type=click.Choice(list(str(n) for n in range(1, len(chapters)+1)))))
chosen_chapter = chapters[chosen-1]

#link for chosen chapter
href = chosen_chapter.find_element(By.XPATH, 'div/div[2]/a').get_attribute('href')
driver.get(href)

#get images
images = driver.find_elements(By.XPATH, '//div[@id="readerContent"]/div/div[2]/img')


time.sleep(60)
driver.quit()

