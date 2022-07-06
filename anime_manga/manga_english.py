from time import sleep
from access_web_methods import save_imgs_as_pdf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Firefox()
driver.get("https://manganato.com/")

search_engine = driver.find_element(by=By.ID, value='search-story')
search_engine.send_keys('attack', Keys.RETURN)

#script = requests.get('https://manganato.com/themes/hm/js/advanced-search.js?v=1.1.2')
#driver.execute_script(script=script.content.decode())

sleep(5)
mangas = {'name':[], 'link':[]}

mangas_available = driver.find_elements(by=By.XPATH, value='//div[@class="search-story-item"]/a[@class="item-img"]')

import click

print('suggested mangas:')
for c, manga in enumerate(mangas_available, start=1):
    print(f"{c}. {manga.get_attribute('title')}")

chosen = click.prompt('\nchoose ', type=click.Choice(list(str(n) for n in range(1, len(mangas_available)+1))))
chosen_manga_link = mangas_available[int(chosen)-1].get_attribute('href')

driver.get(chosen_manga_link)

chapters = driver.find_elements(By.CLASS_NAME, "chapter-name")
chapters.sort()

print()
