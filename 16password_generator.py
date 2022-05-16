# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.

import string
import secrets

def get_size():
    return int(input("Enter desired password length: "))

size = get_size()

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for _ in range(size))

print(password)
