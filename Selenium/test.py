import requests
from bs4 import BeautifulSoup

URL = 'https://pseb.org.pk/app/company_directory_details.php?companyId=NTc='

page = requests.get(URL)
print(page)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.find('title').text)

data = soup.find('div', {'class': 'panel-body'}).text
print(data)

# print("=" * 30)
new_data = [item.replace('\n', '') for item in data]
print(new_data)
# data_list = data.split('\n')
# new_data_list = [item.replace(' ','') for item in data_list]
# print(new_data_list)
