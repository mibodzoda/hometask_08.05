'''import random
a = int(input('Enter the desired password length: '))

for i in range(a):
    print(random.randint(0,a), end='')'''

import string
import random 

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input('Enter the desired password length:'))

print("Generated Password:", generate_password(length))
