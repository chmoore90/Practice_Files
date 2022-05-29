# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the
# dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

# import requests
# from bs4 import BeautifulSoup

# sowpods_url = "https://norvig.com/ngrams/sowpods.txt"

# r = requests.get(sowpods_url)
# soup = BeautifulSoup(r.text, "html.parser")

# with open("sowpods.txt", "w") as sowpods:
#     sowpods.write(str(soup))

import random

with open("sowpods.txt", "r") as sowpods_dict:
    sowpods = sowpods_dict.read()

word = "".join(random.sample(sowpods.split(), 1))

print(word)
