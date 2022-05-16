# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.

import string
import secrets
import requests

# def get_size():
#     return int(input("Enter desired password length: "))

# size = get_size()
# alphabet = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(secrets.choice(alphabet) for _ in range(size))

# print(password)

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def get_strength():
    return input("Choose password strength - weak, medium, or strong: ")

strength = get_strength()

min_word_length = 5

def gen_password ():
    if strength == "weak":
        return gen_weak()
    if strength == "medium":
        return gen_med()
    if strength == "strong":
        return gen_strong()

def gen_word_list():
    word_list = []
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    full_list = response.content.splitlines()
    full_list = [x.decode("utf-8") for x in full_list]
    for y in range(len(full_list)):
        if len(full_list[y]) >= min_word_length:
            word_list.append(full_list[y])
    return word_list

word_list = gen_word_list()

def gen_weak():
    num_of_words = int(input("How many words? "))
    weak_pass = '.'.join(secrets.choice(word_list) for _ in range(num_of_words))

    return weak_pass

def gen_medium():
    chars = input("Use letters or words? ")
    if chars == "letters":
        pass_length = int(input("How many characters? "))
        components = string.ascii_letters + string.digits
        med_pass = ''.join(secrets.choice(components) for _ in pass_length)

        return med_pass

    elif chars == "words":
        pass_length = int(input("How many words? "))
        words = [words.append(secrets.choice(word_list)) for _ in pass_length]
        for x in range (0, pass_length, 2):






password = gen_password()
print(password)
