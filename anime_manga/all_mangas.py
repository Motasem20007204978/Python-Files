from time import sleep
from selenium import webdriver
from csv import DictWriter
import re


driver = webdriver.Firefox(executable_path="C:\driver\geckodriver.exe")
driver.get('https://3asq.org')


try:
    more = driver.find_element_by_class_name('load-title')
    while more:
        print('after 5 seconds')
        more.click()
        sleep(5)
except:
    ...

mangas = driver.find_elements_by_xpath('//*[@class="h5"]/a')
all_mangas = []

for a in mangas:
    href = a.get_attribute('href')
    if re.search(r'^https://3asq.org/manga/[\w\-]+/$', href):
            all_mangas.append({'manga_name': a.text, 'link': href})

with open('all_manga.csv', 'w', encoding='utf-8') as f:
    writer = DictWriter(f=f, fieldnames=['manga_name', 'link'])
    writer.writeheader()
    writer.writerows(rowdicts=all_mangas)

driver.quit()
