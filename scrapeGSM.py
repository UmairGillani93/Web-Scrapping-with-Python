from bs4 import BeautifulSoup
import requests

url = 'https://www.gsmarena.com/samsung_galaxy_s8-8161.php'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify)

#print(soup.find_all('a'))

#print(soup.find(id = 'link1'))

with open('newfile.txt', 'w') as f:
    for link in soup.find_all('a'):
        f.write(link.get('href'))


link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
