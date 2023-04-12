# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on
# this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
# so that you can read the full article without having to click any buttons.

import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)

soup = BeautifulSoup(r.content, 'html.parser')

article_main = soup.find(class_='article main-content')
para_div = article_main.find_all('p')

for para in para_div:
    print(para.text)
