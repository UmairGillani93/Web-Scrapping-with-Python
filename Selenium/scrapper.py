import requests
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver_linux64/chromedriver")

dataframe = pd.DataFrame(columns=['Title'])

# Step:1 Get the URL of the page
driver.get('https://www.indeed.com.pk/jobs?q=software+engineer&l=Islamabad')

# Get all the jobs on that page
jobs = driver.find_elements_by_class_name('result')

for job in jobs:
    result_html = job.get_attribute('innerHTML')
    soup = BeautifulSoup(result_html, 'html.parser')

    try:
        title = soup.find('a', class_='title'),text.replace('\n', '')
    except:
        title = 'None'

dataframe.append({'Title': title}, ignore_index=True)

print(dataframe.head())
