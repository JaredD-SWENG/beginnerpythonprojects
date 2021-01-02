##2.9.2018
##Knock-Knock Joke Teller 2.2.2

'''Peudocode: This program tells the user a "knock knock" joke. It contains to two functions, one to tell a "knock knock" joke and another one to listen to a
"knock knock" joke. It first displays to the user the joke which it has randomly chosen from a wide variety of "knock knock" jokes in its storage.
At the end, it asks the user to tell it a joke and responds accordingly.'''

import random

print('''Welcome to Knock-Knock Joke Teller!
''')

def tell_a_joke():
    joke_part1 = ['Lettuce',
             'Candy',
             'Adore',
             'Nana',
             'Harry',
             'An extraterrestrial',
             'Old lady',
             'Barbara',
            'Tank',
            'Nobel',
            'Boo',
            'Spell',
            'Police',
            'Ash',
            'Waddle',
            'Cash',
            'Snow']
    joke_part2 = ["Lettuce in and I'll tell you.",
                  "Candy door open any slower!",
                  "Adore between us. Open up!",
                  "Nana your business.",
                  "Harry up and answer the door!",
                  "What - how many extraterrestrials do you know?",
                  "I didn't know you could yodel!",
                  "Barbara black sheep have you any candy...!",
                  "Your Welcome.",
                  "No bell, that's why I knocked!",
                  "Don't cry, it's just a joke.",
                  "OK, W_H_O.",
                  "Police can you open the door?",
                  "Bless you!",
                  "Waddle I do with this pizza if you don't open the door?",
                  "No thank you, I'm allergic to nuts.",
                  "Snow use - I've forgoten my name again."]

    print('Knock Knock')
    _ = input('')
    if _.lower() == 'come in' or _.lower() == 'come in.':
        print("Hey, let me finish my joke!")
    jokeNum = random.randint(0,16)
    print(joke_part1[jokeNum])
    _ = input('')
    print(joke_part2[jokeNum])
    print(':D')

def listen_to_a_joke ():
    print('''
Now, you tell me a knock-knock joke.
''')
    _ = input('')
    choice = random.randint(0,1)
    if choice == 1:
        print("Who's there?")
        subject = input('')
        print(subject,'who?')
        _ = input('')
        print(':)')
    elif choice == 0:
        print('''Come in.
XD''')

tell_a_joke()
listen_to_a_joke()
