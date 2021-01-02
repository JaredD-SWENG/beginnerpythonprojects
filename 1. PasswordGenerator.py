import random

print("Password Generator.")

phrase = input("Enter a phrase that you can easily remeber (the longer the phrase the better, also include puncuation): ")
password = ''
characters = 0

for char in phrase.split():
    password += char[0]
password = phrase[-1:] + password + phrase[-1:]
for numbers in range (2):
    numbers = random.randint(0,9)
    password += str(numbers)
for numbers in range (2):
    numbers = random.randint(0,9)
    password = str(numbers)+ password

for char in password:
    characters +=1

while characters < 12:
    print("\nThat password would not be secure.")
    phrase = input("Enter another phrase that you can easily remember (a phrase with 6 words or more would help make a secure password, remember to include punctuation.): ")
    password = ''
    characters = 0
    
    for char in phrase.split():
        password += char[0]
    password = phrase[-1:] + password + phrase[-1:]
    for numbers in range (2):
        numbers = random.randint(0,9)
        password += str(numbers)
    for numbers in range (2):
        numbers = random.randint(0,9)
        password = str(numbers)+ password

    for char in password:
        characters +=1

print("\nPassword: "+password)
