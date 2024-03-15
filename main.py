import Team
from Battle import battle
import Player

players = []
for i in range(12):
    players.append(Player.makeRandomPlayer())
team = Team.Team(players)
players = []
for i in range(12):
    players.append(Player.makeRandomPlayer())
oppTeam = Team.Team(players)

print(battle(team, oppTeam))