import random

from os import system

import utils

key = utils.load_key()

class List:
    def __init__(self, file):
        self.file = file

    def open_list(self):
        system('cls')
        with open(self.file) as pw_lst:
            print(pw_lst.read())
        inp = input('[m] for menu, [q] for quit   ')
        if inp == 'm':
            pass
        else:
            utils.encrypt(self.file, key)
            quit()

    def search_list(self):
        system('cls')
        keyword = input('Which service are you looking for? ')
        with open(self.file, 'r') as fn:
            file = fn.read()
        ind = file.find(keyword)
        if ind == -1:
            print('Keyword not found')
        else:
            print(file[ind:(ind+80)])        
        inp = input('[s] for search again, [m] for menu, [q] for quit   ')
        if inp == 'm':
            pass
        elif inp == 's':
            self.search_list()
        else:
            utils.encrypt(self.file, key)
            quit()

    def add_service(self):
        system('cls')
        service = input('service: ')
        username = input('username: ')
        makepw = input('Do you want a generated password? y or n   ')
        if makepw == 'y':
            password = self.make_password()
            print(f'password: {password}')
        else:
            password = input('password: ')
        new_item = ListService(service, username, password)
        with open(self.file, 'a') as pwlist:
            pwlist.write(str(new_item))
            print('Service was saved to list')
        inp = input('[m] for menu, [q] for quit   ')
        if inp == 'm':
            pass
        else:
            utils.encrypt(self.file, key)
            quit()

    def make_password(self, length=random.randint(5,6)):    
        inp = input("Do you want an easy password? y or n  ")
        if inp == 'y':
            pw = self.make_easy_password()
        else:
            letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
            numbers = [number for number in range(10)]
            symbols = [symbol for symbol in '#$%&!']
            pw = ''
            for _ in range(length):
                pw = pw + letters[random.randint(0,25)]
                num = random.randint(0,1)
                num2 = random.randint(0,3)
                if num:
                    pw = pw + str(numbers[random.randint(0,9)])
                if not num2:
                    pw = pw + symbols[random.randint(0,4)]
        return pw

    def make_easy_password(self):
        return 'easy'

    def update_service(self):
        system('cls')
        service = input('Which service you want to update?  ')
        with open(self.file, 'r') as fn:
            file = fn.read()
        ind = file.find(service)
        if ind == -1:
            print('Service not found')
            return
        else:
            print(file[ind:(ind+80)]) 
        username = input('new username: ')
        makepw = input('Do you want a generated password? y or n   ')
        if makepw == 'y':
            password = self.make_password()
            print(f'new password: {password}')
        else:
            password = input('new password: ')
        update = f'{service}, username: {username}, password: {password}\n'
        updated_file = file.replace(file[ind:(ind+80)], update)
        with open(self.file, 'w') as pwlist:
            pwlist.write(updated_file)
            print('Service was updated')
        inp = input('[m] for menu, [q] for quit   ')
        if inp == 'm':
            pass
        else:
            utils.encrypt(self.file, key)
            quit()


class ListService:
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password
        self.notes = None
        self.name = f'service: {self.service}, username: {self.username}, password: {self.password}\n\
-----------------------------------------------------------------------\n'

    def __repr__(self):
        return self.name

    

    