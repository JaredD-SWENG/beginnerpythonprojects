#5.12.2018
#Battling Creatures Word Game 6.6.2

'''Pseudocode: The program is designed as a word game in which specific character battle each other. It allows the player to choose from a group of character each
with a predetermined health and attack moves (each varying in power). The game will continue as the player and computer each choose an attack and as their opponent's
health lowers. The game will end when one of the players health runs out. The game will end by displaying the winner of the battle to the user.'''

print('''Welcome to Creature Battle! You can choose a creature from the list to use in your battle.
You can then choose from attacks you want to use (enter in the attack number), some are more powerful than others, but the more powerful an attack the more it takes from your health.
Try to get your opponent's health to 0.\n''')

import random
 
class creature:
    '''Battling Creatures
 
    Attributes: name, attack_1, attack_2, attack_3, health
    '''
    def __init__(self, stats):
        self.name = stats[0]
        self.attack_1 = stats[1]
        self.attack_2 = stats[2]
        self.attack_3 = stats[3]
        self.health = 100
 
    def __str__(self):
        return "\n%s's Health: %s" % (self.name, self.health)
 
    def battle(self, opponent, attack):
        '''(object,object,str)-> object.attribute

        Returns opponent's health after subtracting player's attack form it, and returns player's health after subtracting energy lost'''
        if attack == self.attack_1:
            print("\n%s - %s" % (self.name, self.attack_1))
            opponent.health -= random.randint(5,25)
            self.health -= random.randint(0,5)
        elif attack == self.attack_2:
            print("\n%s - %s" % (self.name, self.attack_2))
            opponent.health -= random.randint(10,30)
            self.health -= random.randint(5,10)
        else:
            print("\n%s - %s" % (self.name, self.attack_3))
            opponent.health -= random.randint(15,35)
            self.health -= random.randint(10,15)
        return (opponent.health, self.health)
        
       
def pickAttackMove(charcters, character):
    '''(dict,str)->str

    Returns attack move based on character'''
    pick = 0
    while pick not in [1,2,3]:
        pick = int(input("\nChoose an attack: %s [1], %s [2], %s [3]: " % (characters[character][1],characters[character][2],characters[character][3])))
    if pick == 1:
        pick = characters[character][1]
    elif pick == 2:
        pick = characters[character][2]
    elif pick == 3:
        pick = characters[character][3]
    return pick
  
characters = {"charybdis": ("charybdis", "water blast","hydro vortex", "aqua missle"),
           "hippogriff": ("hippogriff", "aerial assualt", "beak blast", "wing hurricane"),
           "phoenix": ("phoenix", "fire lash", "heat wave", "flame oblivion"),
           "troll":("troll", "mud bomb","hammer smash","bulldoze")}

print("Creatures:\n")
for i in characters.keys():
    print(i)
pick = ""
while pick.lower() not in (characters.keys()):
    pick = input("\nPick a creature: ")
player = creature(characters[pick])
cpu_pick = pick
while cpu_pick == pick:
    cpu_pick = random.choice(list(characters.keys()))
computer = creature(characters[cpu_pick])
print("Computer chose",cpu_pick)
print("\n%s VS %s" % (pick.upper(), cpu_pick.upper()))

first_move = random.choice(['player','computer'])
if first_move == 'player':
        print('\n(You attack first...)')
else:
    print('\n(Computer attacks first...)')

while True:
    print(player)
    print(computer)
    if first_move == 'player':
        attack = pickAttackMove(characters, pick)
        result = player.battle(computer, attack)
        if computer.health <= 0 or player.health <= 0:
            break
        cpu_attack = random.choice([characters[cpu_pick][1],characters[cpu_pick][2],characters[cpu_pick][3]])
        result = computer.battle(player,cpu_attack)
        if player.health <= 0 or computer.health <= 0:
            break
    elif first_move == 'computer':
        cpu_attack = random.choice([characters[cpu_pick][1],characters[cpu_pick][2],characters[cpu_pick][3]])
        result = computer.battle(player,cpu_attack)
        if player.health <= 0 or computer.health <= 0:
            break
        attack = pickAttackMove(characters, pick)
        result = player.battle(computer, attack)
        if computer.health <= 0 or player.health <= 0:
            break
        

print("\nBattle Over")
if player.health > 0:
    print("\nYou win!")
elif computer.health > 0:
    print("\nComputer wins!")
else:
    print("\n You both lose!")
