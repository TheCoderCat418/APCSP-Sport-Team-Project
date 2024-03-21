from names import generateName
from Player import makeRandomPlayer
from random import randint
from Battle import battle 
import randomEvents
from Team import Team, createRandomTeam

battlesLeft = 12
time = 50
team = []
won = 0


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


def playGame():
    global battlesLeft, won
    luckyGuy = randint(0, len(team.team)-1)
    mTeam = team
    mOppTeam = createRandomTeam()
    if(randomEvents.rollRandom(100,1)):
        print(team.team[luckyGuy].name + " lost their voice.")
        mTeam.team[luckyGuy].setCommunication(10)
    if(randomEvents.rollRandom(30,1)):
        print(team.team[luckyGuy].name + " has not showed up. Team score will be down.")
        mTeam.team.pop(luckyGuy)
    if(randomEvents.rollRandom(30,1)):
        print("A member of the other team did not show up.")
        mOppTeam.team.pop(luckyGuy)
    if(battle(mTeam, mOppTeam) == "won"):
        won += 1
    battlesLeft -= 1

def mainMenu():
    print("\"Welcome to the rest area. Have any time to spend?\" said the Time Keeper.")
    print("1. Take your team to the gym. 25 Time Points\n2. Take a rest day 10 Time Points (all players get +10 mood)\n3. Continue to the next game")
    outP = ""
    while(True):
        inpu = input("\n>")
        match (inpu):
            case "1":
                outP = 1
                break
            case "2":
                outP = 2
                break
            case "3":
                outP = 3
                break
            case _:
                print("Invalid. PLease try again.")














while(battlesLeft != 0):
    playGame()
print(won)



    