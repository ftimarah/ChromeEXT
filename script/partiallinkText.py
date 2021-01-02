import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

# scrapes all text from table and returns in txt file
try:
    url = requests.get("https://www.paulaschoice.com/ingredient-dictionary").text
    soup = BeautifulSoup(url, 'lxml')
    # print(soup.prettify())

    table = soup.find('table', {'class':'base'})
    dscrps = table.find_all('p')

    with open('1dscrption.txt', 'w') as outfile:
        outfile.write("\n".join(str(dscrp) for dscrp in dscrps))

except:
    print("Error opening url")

