from Names import generateName
from Player import makeRandomPlayer
from random import randint
from Battle import battle 
import randomEvents
from Teams import Team, createRandomTeam

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
    global battlesLeft, won, time
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
    batter = battle(mTeam, mOppTeam)
    if(batter[0] == "won"):
        print("You won by " + str(round(batter[1])))
        won += 1
        if(round(batter[1]) < 15):
            time += 15
        else:
            time += round(batter[1])
    else:
        print("You lost :(")
        time += 15
    battlesLeft -= 1

def mainMenu():
    global team, time
    print("\"Welcome to the rest area. Have any time to spend?\" said the Time Keeper. You have " + str(time) + " time")
    while(True):
        print("1. Train your team in a certain, random, area. 15 Time Points\n2. Take a rest day. 10 Time Points (all players get +10 mood)\n3. Upgrade all parts of your team by 10 (magic). 25 time points\n4. Continue to the next game")
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
                case "4":
                    outP = 4
                    break
                case _:
                    print("Invalid. PLease try again.")
        areas = ["Communication", "ReactionTime", "Speed", "Strength", "Agility", "Mood",]
        match (outP):
            case 1:
                if(time < 15):
                    print("Not enough credits.")
                    continue
                time -= 15
                print("Your team has been upgreaded")
                area = areas[randint(0, len(areas)-1)]
                print(area + " was upgraded")
                for i in range(len(team.team)):
                    teamMemberData = getattr(team.team[i], 'get'+area)() # https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string Very helpful
                    if(teamMemberData+10 >100):
                        teamMemberData = 100
                    else:
                        teamMemberData += 10
                    getattr(team.team[i], 'set'+area)(teamMemberData)
            case 2:
                if(time < 10):
                    print("Not enough credits.")
                    continue
                time -= 10
                print("Your team is happier")
                for i in range(len(team.team)):
                    teamMemberData = getattr(team.team[i], 'getMood')() # https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string Very helpful
                    if(teamMemberData+10 >100):
                        teamMemberData = 100
                    else:
                        teamMemberData += 10
                    getattr(team.team[i], 'setMood')(teamMemberData)
            case 3:
                if(time < 25):
                    print("Not enough credits.")
                    continue
                time -= 25
                print("Wow")
                for area in areas:
                    for i in range(len(team.team)):
                        teamMemberData = getattr(team.team[i], 'get'+area)() # https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string Very helpful
                        if(teamMemberData+10 >100):
                            teamMemberData = 100
                        else:
                            teamMemberData += 10
                        getattr(team.team[i], 'set'+area)(teamMemberData)
            case 4:
                return
        if time < 10:
            return
        print("Anything else? You still have " + str(time) + " time")

while(battlesLeft != 0):
    mainMenu()
    print("\nPlaying game\n")
    playGame()
print("Season over! You won: " + str(won))


