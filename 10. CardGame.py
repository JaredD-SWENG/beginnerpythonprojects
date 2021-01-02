#4.6.2018
#Card Game 5.2.2

'''Pseudocode: The program is designed to this programme is designed to stimulate simple one player[player versus computer] card game.
The player and computer each gets 5 virtual cards in their list at the beginning of the game. Next, the player and computer will each take turns asking each other
if they have a specific card. If they don't they will be given more virtual cards until they have one that matches. Once they have the cards they matching cards
will be removed from each of their lists. The program uses multiple functions to execute these intstuction. The winner of the game is the player with zero or
the least amount of cards.'''

print('''Welcome to Card Game!
Rules: First, you and the computer each get 5 cards. To start playing, ask the computer if it has a card that is in your deck (e.g. "Do you have a...Queen?").
If the computer has that card, you and the computer will put down all of the cards that match it in each of your decks into a new pile
(e.g You and the computer put down all your Queens).
If the computer does not have that card, it will have to take more cards from the orginal pile, until it has a matching card.
Then you and the computer will put down all of the cards that match it in each of your decks into the new pile.
Next, the computer will ask you if you have a certain card, and if you have it, repeat the previous step.
If you don't have it you will have to take more cards from the orginal pile until it has a matching card.
Again, you and the computer will put down all of the cards that match it in each of your decks into the new pile.
This process repeats until one of you has no more cards, the winner is the one with no cards.
The game can also result in a specific card not in the orginal pile, then the winner will be the player with the least cards.''')

import random

cards =['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']*4
random.shuffle(cards)

def getCards(player_or_computer_cards):
    '''(list)-> str

    Appends items(cards) to a list(player's deck) to populate it until a there is a specific number(5) of items in the list.
    '''
    for i in range(5):
        player_or_computer_cards.append(cards.pop(i))

player_cards = []
getCards(player_cards)
computer_cards = []
getCards(computer_cards)

def getMoreCards(player_or_computer_choice, player_or_computer_cards):
    '''(str, list)-> str

    Appends items(cards) to a list(player's deck) until a specific card is found(other player's choice)
    '''
    while player_or_computer_choice not in player_or_computer_cards:
        if len(cards)==0:
            return 'That card is not in the deck of cards...'
        card = cards.pop(0)
        player_or_computer_cards.append(card)

def getRidOfCards (player_or_computer_choice, player_cards, computer_cards):
    '''(str, list, list) -> list, list

    Removes items(cards) from a list(both players' deck) that match a specific card(the player's choice)
    '''
    while player_or_computer_choice in player_cards:
        player_cards.remove(player_or_computer_choice)
    while player_or_computer_choice in computer_cards:
        computer_cards.remove(player_or_computer_choice)

def findWinner(player_cards, computer_cards):
    '''(list, list) -> str

    Determines the winner by finding which player has the least amount of items(cards) in their list(each players' deck), then displays this information.
    '''
    if len(player_cards) < len(computer_cards):
        print ('You win! The computer had',len(computer_cards),'cards, while you only had',len(player_cards),'cards.')
    elif len(computer_cards) < len(player_cards):
        print ('Computer wins! You had',len(player_cards),'cards, while computer had only',len(computer_cards),'cards.')
    elif len(computer_cards) == len(player_cards):
        print ("It's a tie! You had",len(player_cards),'cards, and the computer had',len(computer_cards),'cards.')

    
while True:
   
    if len(player_cards)== 0 or len(computer_cards) == 0:
        findWinner(player_cards, computer_cards)
        break
    
    print('\nYour cards:', player_cards)
    
    player_choice = input('\nDo you have...(ask the computer if it has a card that is in your deck) ')
    while player_choice not in player_cards:
        player_choice = input('That card is not in your deck, choose a card from your deck: ')        
    
    if player_choice in computer_cards:
        print('Yes.')
        getRidOfCards(player_choice, player_cards, computer_cards)
    else:
        print('No, I have to get more cards...')
        getMoreCards(player_choice, computer_cards)
        if getMoreCards(player_choice, computer_cards) == 'That card is not in the deck of cards...':
            print('That card is not in the deck of cards...')
            findWinner(player_cards, computer_cards)
            break
        print('Now I have one.')
        getRidOfCards(player_choice, player_cards, computer_cards)

    if len(player_cards)== 0 or len(computer_cards) == 0:
        findWinner(player_cards, computer_cards)
        break
            
    print('\nYour cards:', player_cards)
    
    computer_choice = random.choice(computer_cards)
    print('\nDo you have', str(computer_choice)+'?')
    
    if computer_choice in player_cards:
        answer = input('')
        getRidOfCards(computer_choice, player_cards, computer_cards)
    else:
        answer = input('')
        print('You need to get more cards...')
        getMoreCards(computer_choice, player_cards)
        if getMoreCards(computer_choice, player_cards) == 'That card is not in the deck of cards...':
            print('That card is not in the deck of cards...')
            findWinner(player_cards, computer_cards)
            break
        print('Your cards:', player_cards)
        print('Now you have one')
        getRidOfCards(computer_choice, player_cards, computer_cards)
    
