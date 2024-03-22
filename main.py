import Teams
from Battle import battle
import Player
from Leveler import levelUpPlayer
import randomEvents
players = []
for i in range(12):
    players.append(Player.makeRandomPlayer())
team = Teams.Team(players)
print(team.getTeamAverage())
team = levelUpPlayer(team, 1, "speed", team.team[1].getSpeed()+1)
print(team.getTeamAverage())


players = []
for i in range(12):
    players.append(Player.makeRandomPlayer())
oppTeam = Teams.createRandomTeam()

print(battle(Teams, oppTeam))

wins = 0
for i in range(5):
    if(randomEvents.rollRandom(5,1)):
        wins+=1
print((wins/5)*100)
