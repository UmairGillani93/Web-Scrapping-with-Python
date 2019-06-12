from bs4 import BeautifulSoup
from urllib.request import urlopen as open

url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

client = open(url)
print(client)

soup = BeautifulSoup(client, 'html.parser')
#print(soup.title)

containers = soup.findAll('div', {'class', 'bhgxx2 col-12-12'})
#print(len(containers))
#print(containers[0])
#print(containers[1])

print(soup.prettify(containers))

# now let's extract the information of a particular Phone
# this information includes -> Title, price, ratings etc

container = container[0]

print(container.div.image['alt']) # reports back the title of the Phone

price = container.findAll('div', {'class':'bhgxx2 col-12-12'})
print(price[0].text)

ratings = soup.findAll('div', {'class':'bhgxx2 col-12-12'})
print(ratings[0].text)

# now lets save this entire information into a CSV file

file_name = 'products.csv'
f = open(file_name, 'w')
headers = 'ProductName, Price, Ratings\n'
f.write(headers)

for container in containers:
    product_name = container.div.img['alt']
    price_contiainer = container.findAll('div', {'class': 'bhgxx2 col-12-12'})
    price = price_contiainer[0].text.strip()
    rating_container = container.findAll('div', {'class': 'bhgxx2 col-12-12'})
    rating = rating_container[0].text.strip()

    print('Product Name: ', product_name)
    print('Price: ', price)
    print('Rating: ', rating)
