import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

# finds all titles from the links from the table in URL and returns in text 1DESCRIPTION.TXT

#--------------------------------------------------------------------
#issue: links have the title and category of the ingredient/substance within the url tag, and currently not able to extract it from outside the link
# therefore just manually find all and deleteing the urls to scrape for the titles. 
#so this is technically the code to get the titles and the type of substance but through the link href tag
#--------------------------------------------------------------------

try:
    url = requests.get("https://www.paulaschoice.com/ingredient-dictionary").text
    # page = urlopen(url)
except:
    print("Error opening url")

soup = BeautifulSoup(url, 'lxml')

table = soup.find('table', {'class':'base'})
titles = table.find_all('h2')
print(titles)

with open('1description.txt', 'w') as outfile:
    outfile.write("\n".join(str(title) for title in titles))
