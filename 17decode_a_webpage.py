# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

base_url = "https://www.nytimes.com/"
r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')
title_list_set = [soup.find_all("h3")]

for title_set in title_list_set:
    for title in title_set:
        print(title.get_text())
