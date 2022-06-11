from selenium import webdriver
from selenium.webdriver.common.by import By
import json

actors = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()
    actors.append(ele)

Path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(Path)

site = 'https://www.imdb.com/'

data = {}

for actor in actors:
    driver.get(site)

    #opening actor's page
    sbox = driver.find_element(by=By.ID, value='suggestion-search')
    sbox.send_keys(actor)
    driver.implicitly_wait(20)
    option1 = driver.find_element(by= By.XPATH, value='//li[@class="react-autosuggest__suggestion react-autosuggest__suggestion--first"]/a')
    option1.click()


    filmography_odd = driver.find_elements(by=By.XPATH, value='//div[@class="filmo-row odd"]')
    filmography_even = driver.find_elements(by=By.XPATH, value='//div[@class="filmo-row even"]')

    films_list = {}
    iter = 0
    for p in range(len(filmography_odd)):
        films_list[iter] = filmography_odd[p].text
        iter+= 1
        if p < len(filmography_even):
            films_list[iter] = filmography_even[p].text
            iter+=1
    
    data[actor] = films_list
    driver.quit()

with open('filmography_data.json', 'w') as f:
    json.dump(data, f)
