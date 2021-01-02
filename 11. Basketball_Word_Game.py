#4.22.2018
#Basketball Word Game 5.2.2

'''Pseudocode: The program is designed as a basketball word game. It simulates a simple one player[player versus computer] basketball word game.
The player and computer each get turn with possesion of the ball, they can choose to dribble, pass, or shoot the ball. The first team to reach 5 points wins the
game.'''

import random
import time

urteam_score = 0
otherteam_score = 0

shooting_options = ['The shot makes it', 'The shot does not makes it']
stealing_options = ['The ball is stolen', "Ball is not stolen"]
defensive_options = ['Your team steals the ball','The other team shoots the ball']

def defensivegameplay():
    '''()-> str

    Returns multiple strings describing a basketball game and switches into other functions based on inputs from user.'''
    global urteam_score
    global otherteam_score
    while urteam_score < 5 and otherteam_score < 5:
        time.sleep(1.5)
        print('\nThe other team has possesion of the ball')
        options = random.choice(defensive_options)
        if options == 'Your team steals the ball':
            time.sleep(1.5)
            print(options)
            time.sleep(1.5)
            urteam_score +=1            
            print('\nYou score a point')
            print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
            defensivegameplay()
        else:
            time.sleep(1.5)
            print(options)
            options = random.choice(shooting_options)
            if options == 'The shot makes it':
                time.sleep(1.5)
                print(options)
                otherteam_score +=1
                print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
                offensivegameplay()
            else:
                time.sleep(1.5)
                print(options)
                offensivegameplay()
                
def offensivegameplay():
    '''()->str

    Returns multiple strings describing a basketball game and switches into other functions based on inputs from user.'''
    global urteam_score
    global otherteam_score
    while urteam_score < 5 and otherteam_score < 5:
        print('\nYou have possesion of the ball')
        choice = input('\nDo you want to dribble, pass, or shoot: ')
        if choice.lower() == 'dribble':
            options = random.choice(stealing_options)
            if options == 'The ball is stolen':
                time.sleep(1.5)
                print(options)
                time.sleep(1.5)
                otherteam_score+=1
                print('\nOther team scores a point')
                print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
                offensivegameplay()
            else:
                choice = input('\nYou still have the ball, do you want to pass or shoot: ')
                if choice.lower() == 'pass':
                    time.sleep(1.5)
                    print('\nYour teammate shoots the ball')
                    options = random.choice(shooting_options)
                    if options == 'The shot makes it':
                        time.sleep(1.5)
                        print(options)
                        urteam_score +=1
                        print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
                        defensivegameplay()
                    else:
                        time.sleep(1.5)
                        print(options)
                        defensivegameplay()
                elif choice.lower()== 'shoot':
                    options = random.choice(shooting_options)
                    if options == 'The shot makes it':
                        time.sleep(1.5)
                        print(options)
                        urteam_score +=1
                        print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
                        defensivegameplay()
                    else:
                        time.sleep(1.5)
                        print(options)
                        defensivegameplay()
        elif choice.lower() == 'pass':
            time.sleep(1.5)
            print('\nYour teammate shoots the ball')
            options = random.choice(shooting_options)
            if options == 'The shot makes it':
                time.sleep(1.5)
                print(options)
                urteam_score +=1
                print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
                defensivegameplay()
            else:
                time.sleep(1.5)
                print(options)
                defensivegameplay()
        elif choice.lower() == 'shoot':
            options = random.choice(shooting_options)
            if options == 'The shot makes it':
                time.sleep(1.5)
                print(options)
                urteam_score +=1
                print("\nYour score is", urteam_score, "and the other team's score is", otherteam_score)
                defensivegameplay()
            else:
                time.sleep(1.5)
                print(options)
                defensivegameplay()

def find_winner():
    '''() -> str

    Returns string displaying the winner of the game.'''
    global otherteam_score
    global urteam_score
    if urteam_score > otherteam_score:
        print("\nYour team wins!")
    else:
        print("\nThe other team wins!")


offensivegameplay()
find_winner()

