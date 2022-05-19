# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (Extra 1: Write both .txt lists as new files.)

import requests

# from bs4 import BeautifulSoup

prime_url = "https://www.practicepython.org/assets/primenumbers.txt"
happy_url = "https://www.practicepython.org/assets/happynumbers.txt"

r_prime = requests.get(prime_url)
r_happy = requests.get(happy_url)

p_text = (r_prime.text)
h_text = (r_happy.text)

p_list = p_text.splitlines()
h_list = h_text.splitlines()
overlap = []

# for x in p_list:
#     if x in h_list and x not in overlap:
#         overlap.append(x)

[overlap.append(x) for x in p_list if x in h_list and x not in overlap]


print(overlap)
