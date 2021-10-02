import configparser

from os import system
from passlib.context import CryptContext

import utils

import classes

context = CryptContext(schemes=["pbkdf2_sha256"], default="pbkdf2_sha256", pbkdf2_sha256__default_rounds=10000)
decrypt = False
config = configparser.ConfigParser()
config.read('config.txt')

access = config['pwm']['password']
list_name = config['pwm']['list']

i = 0
for _ in range(3):
    inp = input('manager password: ')
    check = context.verify(inp, access)
    if check:
        login = True
        break
    else:
        login = False
        i += 1
        if i == 3:
            print('Three failures.\nStart program again.')
            quit()
        print('Wrong Password. Try Again.')

my_list = classes.List(list_name)

key = utils.load_key()

while True:
    if login:
        if decrypt == False:
            utils.decrypt(list_name, key)
            decrypt = True
        system('cls')
        choice = utils.menu()       

    if choice == 1:
        my_list.open_list()
    elif choice == 2:
        my_list.search_list()
    elif choice == 3:
        my_list.add_service()
    elif choice == 4:
        my_list.update_service()
    else:
        utils.encrypt(list_name, key)
        quit()

