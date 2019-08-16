import random
import string

def passwordGenerate():
    x = string.ascii_letters + string.digits + string.punctuation
    i = 0
    password = ""
    while i < 12:
        i = i + 1
        password = password + random.choice(x)
    return (password)

print (passwordGenerate())