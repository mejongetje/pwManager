from passlib.context import CryptContext

import utils

context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=10000
)

# 1. choose password
pw = input('Choose your password: ')
encr_pwd = context.hash(pw)

# 2. give name to list
inp = input('Choose a name for your list: ')
list_name = str(inp + '.txt')

# 3. Make a config file
string = str('[pwm]' + '\n' + 'password = ' + encr_pwd + '\n' + 'list = ' + list_name)

with open('config.txt', 'w') as fn:
    fn.write(string)

# 4. Make a list file

with open(list_name, 'x') as fn:
    pass

# 5. make a key file
utils.write_key()

# 6. encrypt list
key = utils.load_key()
utils.encrypt(list_name, key)

