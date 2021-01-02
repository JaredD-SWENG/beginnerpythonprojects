#2.25.2018
#Secret Cipher 5.4.6

'''Pseudocode: The program is designed to take an inputed message and convert it into a secret message, as well as take the secret message and turn it back into the
actual message.It does this by asking the user for a message, and then randomly chooses a arrangement of characters.It also randomly chooses a key.
Finally the program displays the encrypted message, key, and arrangement number.
To use the decryption function in the program, the user must enter the secret message, key, and arrangment number. The program will then decrypt the message, and
display it to the user. What makes this encrypter unquie is that you can display the message, key and arrangment number publically. Only the person with the different
arrangements will be able to decipher the message.'''

def Encrypt ():
    import random
    arrangement_choices=["0123456789ABabCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "ABabCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz.!@#%^&*_-+=`~?',;:/\|()[]{}$ 0123456789",
                ".!@#%^&*_-+=`~?',;:/\|()[]{}$ 0123456789abcABCdefDEFghiGHIjklJKLmnoMNOpqrPQRstuSTUvwxVWXyzYZ"]
    arrangement_num = random.randint(0,5)
    characters = arrangement_choices[arrangement_num]
    key = random.randint(-91,91)
    message=input("message: ")
    newmessage=""
    for char in message:
        position = int(characters.find(char))
        newposition = (position + key)%92
        newchar = characters[newposition]
        newmessage += newchar
    print("secret message:",newmessage)
    print("arrangement:",arrangement_num)
    print("key:",key)

def Decrypt ():
    arrangement_choices=["0123456789ABabCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.!@#%^&*_-+=`~?',;:/\|()[]{}$ ",
                "ABabCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz.!@#%^&*_-+=`~?',;:/\|()[]{}$ 0123456789",
                ".!@#%^&*_-+=`~?',;:/\|()[]{}$ 0123456789abcABCdefDEFghiGHIjklJKLmnoMNOpqrPQRstuSTUvwxVWXyzYZ",
                         ]
    message=input("secret message: ")
    arrangement_num = int(input("arrangement: "))
    characters = arrangement_choices[arrangement_num]
    key = int(input("key: "))
    newmessage=""
    for char in message:
        position = int(characters.find(char))
        newposition = (position - key)%92
        newchar = characters[newposition]
        newmessage += newchar
    print("message:",newmessage)

print('''Welcome to Secret Cipher!
''')
function = ''
while function.lower() != "done":
    function = input('Encrypt, decrypt, or done: ')
    print("")
    if function.lower() == "encrypt":
        print("Encrypter")
        Encrypt()
        print("")
    elif function.lower() == "decrypt":
        print("Decrypter")
        Decrypt()
        print("") 
        
