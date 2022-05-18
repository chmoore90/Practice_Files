# # Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the
# # results to the screen. I have a .txt file for you, if you want to use it (https://www.practicepython.org/assets/nameslist.txt)!

# # Extra 1 (personal): Create a new file to read from by scraping from the example .txt file provided.

import requests
from bs4 import BeautifulSoup

# base_url = "https://www.practicepython.org/assets/nameslist.txt"
# r = requests.get(base_url)

# soup = BeautifulSoup(r.text, "html.parser")

# with open("nameslist.txt", "w") as names_write:
#     soup_string = str(soup)
#     names_write.write(soup_string)


# # Begin exercise:

# with open("nameslist.txt", "r") as names_read:
#     all_text = names_read.read()

# all_text_list = all_text.splitlines()
# all_text_set = set(all_text_list)

# for x in all_text_set:
#      y = all_text_list.count(x)
#      print(f"{x}: {y}")


# Extra 2: Instead of using the .txt file from above, take this .txt file (https://www.practicepython.org/assets/Training_01.txt)
# and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the
# SUN database scene recognition database, and lists the file directory hierarchy for the images.

# Extra 3 (personal): Create a new file to read from by scraping from this .txt as well.

base_url2 = "https://www.practicepython.org/assets/Training_01.txt"
r2 = requests.get(base_url2)

soup2 = BeautifulSoup(r2.text, "html.parser")

with open("SUNlist.txt", "w") as sun_write:
    soup_string2 = str(soup2)
    sun_write.write(soup_string2)

# Begin exercise:

with open("SUNlist.txt", "r") as sun_read:
    cat_count = {}
    line = sun_read.readline()[3:-26]
    while line:
        if line in cat_count:
            cat_count[line] += 1
        elif line not in cat_count:
            cat_count[line] = 1
        line = sun_read.readline()[3:-26]
    print(cat_count)
