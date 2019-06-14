from bs4 import BeautifulSoup
import requests

url = requests.get('https://redditmetrics.com/top')

soup = BeautifulSoup(url.text, 'html.parser')

print(soup.title)

with open('reddit.txt', 'w') as f:

    for sub_reddit in soup.find_all('a'):
        try:
            if '/r/' in sub_reddit.string:
                f.write(sub_reddit.string[3:] + '\n')

        except:
            TypeError
