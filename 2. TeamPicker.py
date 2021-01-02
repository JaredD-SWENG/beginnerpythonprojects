#12.1.2017
#Team Picker 1.2.6

'''Pseudocode: The program is designed to organize a group of people into teams.
It does this by asking the user for the names of the people and the number of teams desired.
With these pieces of information, the program puts different people in different teams, and displays the teams to the user.
It even lets the user know which people were unable to be fit into one of the teams.'''


import random

print('''Welcome to Team Picker!
''')

People = input("Enter the names of the people (seperated by comma and space): ")
PeopleList = list(People.split(', '))
AmountPeople = len(PeopleList)
print("You have",AmountPeople,"people on this list.")
TeamNum = int(input("Enter number of teams: "))
Teams = list(range(1, TeamNum+1))
AmountTeams = len(Teams)
while AmountTeams > AmountPeople:
    print('''The amount of teams cannot be greater than the number of people.
Enter valid options.''')
    People = input("Enter the names of the people(seperated by comma and space): ")
    PeopleList = list(People.split(', '))
    AmountPeople = len(PeopleList)
    TeamNum = int(input("Enter number of teams: "))
    Teams = list(range(1, TeamNum+1))
    AmountTeams = len(Teams)

print("")
for T in Teams:
    print("Team "+str(T)+":")
    for Times in range(AmountPeople//AmountTeams):
        Team = random.choice(PeopleList)
        PeopleList.remove(Team)
        print(Team)
    print("")
    
if len(PeopleList) != 0:
    print("Sorry, the following person/people had to be left out:") 
    for i in range (len(PeopleList)):
        print(PeopleList[i])
