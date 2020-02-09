import requests 
from bs4 import BeautifulSoup 

def parse_linkedin(URL):
    page = requests.get(URL)
    print(page)

parse_linkedin("https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin")
