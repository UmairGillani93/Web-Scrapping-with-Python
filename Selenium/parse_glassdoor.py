import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import os
import pandas as pd

df = pd.DataFrame(columns=['Company Name'])

URL = 'https://www.glassdoor.com/Overview/Working-at-S-and-P-Global-EI_IE1259396.11,25.htm'

driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')
driver.get(URL)
time.sleep(10)

html = driver.page_source

# print(html)

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())
# print(soup.find('title'))
#
# comp_title = soup.find('span', {'id': 'DivisionsDropdownComponent'}).text
# website = soup.find('span', {'class': 'value website'}).find('a', href=True)['href']
# headquaters = soup.find('span', {'class': 'value'})

# print(headquaters)

# blocks = soup.find_all('div', {'class': 'info flexbox row col-hh'})
#
# for block in blocks:
#     block.find('div', {'class': 'infoEntity'}).text

# data = soup.find('div', {'class': 'info flexbox row col-hh'})
#
# head = data.find('class.infoEntity[label*=Headquaters]')
# print(head)
# headquaters = soup.find('div', {'class': 'infoEntity'}).find('span', {'class': 'value'}).text
# print(headquaters)
#
# headcounts = soup.find('div', {'class': 'infoEntity'}).find('span', {'class': 'value'}).text
# print(headcounts)

# website = data.find('a', href=True)['href']
# print(website)
#
# headquater = data.find('span', {'class': 'value'}).text
# print(headquater)
# data_dict = {}
#
data = soup.findAll('span', {'class': 'value'})
data_list = [item.text for item in data]
competitors = soup.find('div', {'class': 'pb-std pb-md-0'}).text
data_list.append(competitors)
print('=' * 50)
print(data_list)

# df = pd.DataFrame(data_list, index=['Website', 'Headquaters', 'Size', 'Founded', 'Type', 'Industry', 'Revenue', 'Competitors'], columns=['Teradata'])
# print(df)
# df.to_csv(r'./glassdoor.csv')

# reviews = soup.find('span', {'class': 'subtle'}).text
# print(reviews)
