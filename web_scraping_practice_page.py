# Following tutorial on https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/

import requests
from bs4 import BeautifulSoup

base_url = 'https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html'
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

text = soup.select('div p')
print(text)
