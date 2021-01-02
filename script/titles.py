import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# finds all link titles from table and returns in text file description
#dec 30 2020 5:41pm doesnt work lol

try:
    url = requests.get("https://www.paulaschoice.com/ingredient-dictionary").text
    # page = urlopen(url)
except:
    print("Error opening url")

soup = BeautifulSoup(url, 'lxml')
# print(soup.prettify())

p = re.compile(" >" )
table = soup.find('table', {'class':'base'})
titles = table.find_all('h2')
print(titles)

lst = []
for link in titles:
    if link is None:
        continue
    if p.match(link.get(titles)) is not None:
        lst.append(link.get(titles))

with open('titles.txt', 'w') as outfile:
    for line in lst:
        outfile.write("".join(str(line) + "\n"))