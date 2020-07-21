# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LOWER_CASES = string.ascii_lowercase #Lisa de minúsculas
UPPER_CASES = string.ascii_uppercase #lista de mayúsculas
NUMBERS = string.digits #lista de números


def generate_password():
    # Start coding here
    password = ""
    password_list = random.sample(SYMBOLS, random.randint(2,4))+random.sample(LOWER_CASES, random.randint(2, 4))+random.sample(UPPER_CASES, random.randint(2, 4))+random.sample(NUMBERS, random.randint(2,4))#random para generar resultados aleatorios entre un numero y el otro, random sample para sacar una muestra
    password = password.join(password_list) #concatenar texto
    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')
    
    #print(password)


if __name__ == '__main__':
    run()
