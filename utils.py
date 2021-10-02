from cryptography.fernet import Fernet
from os import system


def menu():
    x = True
    choice_list = [1,2,3,4,5]
    while x == True:
        system('cls')
        print('|-------------------------------------|')
        print('|   P A S S W O R D   M A N A G E R   |')
        print('|-------------------------------------|')
        print('|                                     |')
        print('|   [1] Open List                     |')
        print('|   [2] Search List                   |')
        print('|   [3] Add Service                   |')
        print('|   [4] Update Service                |')
        print('|   [5] Close                         |')
        print('|                                     |')
        print('|-------------------------------------|')
        try:
            choice = int(input('Make your choice: '))
            if choice in choice_list:
                x = False
                return choice
        except:
            print('Option not available.')
            inp = input('Click enter and try again   ')
            

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)



    