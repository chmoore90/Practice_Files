# Take the code from the How To Decode A Website exercise, and instead of printing the results to a screen,
# write the results to a txt file. In your code, just make up a name for the file you are saving to.

# From ex. 17:
import requests
from bs4 import BeautifulSoup

base_url = "https://www.nytimes.com/"
r = requests.get(base_url)

soup = BeautifulSoup(r.content, 'html.parser')
title_list_set = [soup.find_all("h3")]

# for title_set in title_list_set:
#     for title in title_set:
#         print(title.get_text())

# New code:

with open("NY_titles.txt", "w") as NY_titles:

    for title_set in title_list_set:
        for title in title_set:
            title_string = str(title.get_text())
            NY_titles.write(title_string)
            NY_titles.write("\n")
