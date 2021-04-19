import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#-----------------------------------------------------------------------------------------
# code that grabs links from table
# then stores it in an array and writes it to links.txt file loops through every single link to find the <p> description from each link. 
# writes it to links_text.txt file
#-----------------------------------------------------------------------------------------

try:
    url1 = requests.get("https://www.paulaschoice.com/ingredient-dictionary").text
    # page = urlopen(url)
except:
    print("Error opening url")

soup = BeautifulSoup(url1, 'lxml')
p = re.compile("https://www.paulaschoice.com/ingredient-dictionary/")
table = soup.find('table', {'class':'base'})
links = table.find_all('a')
print(len(links))

# loop through each tag and extract link and put into urls array and then put into a text file
urls = []
for link in links:
    if link is None:
        continue
    if p.match(link.get('href', '')) is not None:
        urls.append(link.get('href'))
print(len(urls))

with open('link_urls.txt', 'w') as outfile:
    for line in urls:
        outfile.write(''.join(str(line) + '\n'))

# loop through the array of links and extract any text from inside the <p> tag from ea. link and put in new array then txt file
lst = []

for u in urls:
    try:
        response = requests.get(u).text
        soup = BeautifulSoup(response,'lxml')
        newurl = soup.find('div', {'class': 'upper-body'}).find_all('p')
        lst.append(newurl)
        print(len(lst))
        
        with open('link_text.csv', 'w') as outfile:
            for line in lst:
                outfile.write(''.join(str(line) + '\n'))    

    except AttributeError: 
        print('att err')
        # print("attribute error cuz no description" + str(lst)   )
        continue
