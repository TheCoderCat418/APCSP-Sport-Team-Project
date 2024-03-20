from names import generateName
from Player import makeRandomPlayer
from random import randint
from Battle import battle 
import randomEvents
from Team import Team, createRandomTeam

battlesLeft = 12
time = 50
team = []

def playGame():
    global battlesLeft
    print(battle(team, createRandomTeam()))
    battlesLeft -= 1

def randomEventInGame():
    count = 0
    while(not randomEvents.rollRandom(100,1)):
        count+=1
    print(count)
wins = 0
for i in range(100):
    if(randomEventInGame()):
        wins+=1
print((wins/100)*100)
randomEventInGame()
print("Welcome! It's a new season. Pick 12 people to add to your team!")
while len(team) < 12:
    selectedPlayer = makeRandomPlayer()
    selectedName = generateName()
    while True:
        responce = input(
            f"Name: {selectedName[0]}\nAge: {randint(13,19)}\nGender: {"Male" if selectedName[1] else "Female"}\nCommunication: {selectedPlayer.getCommunication()}\nMood: {selectedPlayer.getMood()}\nReation Time: {selectedPlayer.getReactionTime()}\nSpeed: {selectedPlayer.getSpeed()}\nAgility: {selectedPlayer.getAgility()}\nStrength: {selectedPlayer.getStrength()}\nWould you like this player on your team? You have {12-len(team)} spots left. (Y/n) "
        )
        if(responce.upper() == "Y"):
            print("This player has been added to your team.")
            selectedPlayer.setName(selectedName[0])
            team.append(selectedPlayer)
            break
        elif(responce.upper() == "N"):
            print("Next!")
            break
        print("Invaild input. Please try again.")
team = Team(team)




    