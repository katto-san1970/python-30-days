import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

print("Ваш пароль: ", generate_password(12))
print("Ваш пароль: ", generate_password(8))
print("Ваш пароль: ", generate_password(16))

