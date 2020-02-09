import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import os
import pandas as pd

df = pd.DataFrame(columns=['Company Name'])

URLS = ['https://www.glassdoor.com/Overview/Working-at-Teradata-EI_IE14638.11,19.htm',
        'https://www.glassdoor.com/Overview/Working-at-S-and-P-Global-EI_IE1259396.11,25.htm',
        'https://www.glassdoor.com/Overview/Working-at-IBM-EI_IE354.11,14.htm',
        'https://www.glassdoor.com/Overview/Working-at-IBEX-Global-EI_IE677903.11,22.htm']

for url in URLS:

    driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')
    driver.get(url)
    time.sleep(10)
    # get the html and JS content
    html = driver.page_source
    # print(html)
    # convert the content into soup object for further extraction
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
    content = []
    data = soup.findAll('span', {'class': 'value'})
    info = [item.text for item in data]
    try:
        competitors = soup.find('div', {'class': 'pb-std pb-md-0'}).text
        info.append(competitors)

    except:
        competitors = None
    print('=' * 50)
    print(info)
    content.append(info)
    print(content)

    # df = pd.DataFrame()
    # print(df)
    # df.to_csv(r'./glassdoor.csv')

# print(df)
