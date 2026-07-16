import string
import secrets

def generator_password(length,uppercase,numbers,symbols):
    pool= string.ascii_lowercase
    if uppercase:
        pool+=string.ascii_uppercase
    if numbers:
        pool+=string.digits
    if symbols:
        pool+=string.punctuation

    password = ''.join(secrets.choice(pool) for _ in range(length))  

    return ''.join(password) 

