import Team
from Battle import battle
import Player
from Leveler import levelUpPlayer
players = []
for i in range(12):
    players.append(Player.makeRandomPlayer())
team = Team.Team(players)
print(team.getTeamAverage())
team = levelUpPlayer(team, 1, "speed", team.team[1].getSpeed()+1)
print(team.getTeamAverage())


players = []
for i in range(12):
    players.append(Player.makeRandomPlayer())
oppTeam = Team.Team(players)

print(battle(team, oppTeam))