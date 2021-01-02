##1.18.2018
##Presidential History Quizzer 5.4.6


'''Peudocode: This program quizes people on the order of the presidents. It displays to the user two presidents and asks them
who was president first. It then checks if the user's answer is right or wrong. At the end of the quiz the program will display the user's
score'''

import random

print("Welcome to Presidential History Quizzer!")

num_questions = int(input("How many questions would you like? "))

print('''
Enter the person who became President first.''')

score = 0

presidents = ["Donald J. Trump",
              "Barack Obama",
              "George W. Bush",
              "William J. Clinton",
              "George H. W. Bush",
              "Ronald Reagan",
              "James Carter",
              "Gerald R. Ford",
              "Richard M. Nixon",
              "Lyndon B. Johnson",
              "John F. Kennedy",
              "Dwight D. Eisenhower",
              "Harry S. Truman",
              "Franklin D. Roosevelt",
              "Herbert Hoover",
              "Calvin Coolidge",
              "Warren G. Harding",
              "Woodrow Wilson",
              "William Howard Taft",
              "Theodore Roosevelt",
              "William McKinley",
              "Grover Cleveland",
              "Benjamin Harrison",
              "Chester A. Arthur",
              "James Garfield",
              "Rutherford B. Hayes",
              "Ulysses S. Grant",
              "Andrew Johnson",
              "Abraham Lincoln",
              "James Buchanan",
              "Franklin Pierce",
              "Millard Fillmore",
              "Zachary Taylor",
              "James K. Polk",
              "John Tyler",
              "William Henry Harrison",
              "Martin Van Buren",
              "Andrew Jackson",
              "John Quincy Adams",
              "James Monroe",
              "James Madison",
              "Thomas Jefferson",
              "John Adams",
              "George Washington"]

def Right_Wrong(x, y):
    global score
    if presidents.index(x) > presidents.index(y):
        print("Your right!")
        score += 1
    else:
        print("Your wrong!")
        
for questions in range(num_questions):
    president1 = random.choice(presidents)
    president2=president1
    while president1==president2:
        president2 = random.choice(presidents)

    print(president1, "or", president2+"?")
    answer = input("Answer: ")

    while answer != president1 and answer != president2:
        print("Invalid option.")
        answer = input("Answer: ")
        
    if answer == president1:
        Right_Wrong(president1,president2)
    elif answer == president2:
        Right_Wrong(president2,president1)     

if score >= (num_questions/2):
    print("Great Job! You got "+str(score)+" out of "+str(num_questions)+".")
else:
    print("Meh... You got "+str(score)+" out of "+str(num_questions)+".")
