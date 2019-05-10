import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.hubertiming.com/results/2017GPTR10K'
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

print(soup.prettify().split('\n'))

len(soup.prettify().split('\n')) # total number of elements in list
type(soup)
type(soup.prettify())

print(soup.title)
soup.get_text(separator = '\n', strip = True)

soup.find_all('a') # find_all() extracts all the important html tags, e.g, <a> for hyperlinks <table> for tables,
# <tr> for table rows, <td> for table cells, <th> for table headers

len(soup.find_all('a')) # only 10 hyperlinks in our html page

all_links = soup.find_all('a')

for link in all_links:
    print(link.get('href'))

    # sometimes we have links attributes in <a> tag as 'class', 'names' or 'scr'
    # in order to get hyperlink we can try the above code to get only 'href' attributes of aur <a> tags

rows = soup.find_all('tr')
print(rows[:10])

headers = soup.find_all('td')
print(headers[:10])

# our goal is to calculate grab this DataFrame from web and convert it into Pandas DataFrame for easy manipulations
# to get there need to get all the table rows in list form first

for row in rows:
    row_td = row.find_all('td')
    print(row_td)
    type(row_td)

    # as you can see the data is in html tags form now, and we don't need this
    # lets go ahead and remove those tags from from our data

str_cells = str(row_td)
clean_text = BeautifulSoup(str_cells, 'lxml').get_text()

print(clean_text)
type(clean_text)

# now we need to remove characters from our 'td' tags for all the rows
# for this lets use 're' library

import re

list_rows = []

for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '', str_cells))
    list_rows.append(clean2)

print(list_rows)
print(type(list_rows))

df = pd.DataFrame(data = list_rows) # now lets convert this list, in Pandas DataFrame

print(df.head(10)) # and here's our DataFrame

# The data is still not in our requied form
# lets go ahead and split our DataFrame on commas

df1 = df[0].str.split(',', expand = True)

# this could work, but the data has [ bracke at the begining of each row.
# lets try to tackle this issue as well

df1[0] = df1[0].str.strip('[')
df1.head()

# the table is missing table headers
# so for this let's try to put headers on each column

col_labels = soup.find_all('th')

headers = []

col_str = str(col_labels)
cleanHeader = BeautifulSoup(col_str, 'lxml').get_text()
headers.append(cleanHeader)

print(headers)

df2 = pd.DataFrame(data = headers)
df2
type(df2)

df3 = df2[0].str.split(',', expand=True)
df3.head()

frames = [df3, df1]

df4 = pd.concat(frames) # lets go ahead and concat our newly created DataFrames

df5 = df4.rename(columns = df4.iloc[0]) # assigning first row of df4 as columns
print(df5.head())
# lets see if our DataFrame has any null values

df5 = df5.dropna(axis = 0, how = 'any')

df7 = df5.drop(df5.index[0])
df7.head()
