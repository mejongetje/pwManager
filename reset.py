import utils

key = utils.load_key()

list_name = input("Give the name of the list you want to encrypt? ")

try: 
    f = open(list_name, "r")
    check = f.read(4)
    if check =="serv":
        utils.encrypt(list_name, key)
    else:
        print("The list is already encrypted.")
        quit()

except FileNotFoundError:
    print('Wrong name')

finally:
    quit()


