# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the
# dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

import requests
from bs4 import BeautifulSoup

sowpods_url = "https://norvig.com/ngrams/sowpods.txt"

r = requests.get(sowpods_url)
soup = BeautifulSoup(r.text, "html.parser")

sowpods = str(soup).splitlines()

import random


def get_word():

    word = "".join(random.sample(sowpods, 1))

    return word


print(get_word())
