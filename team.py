class Team:
    def __init__(self, players: list):
        if(len(players) == 12):
            self.team = players
            for i in range(len(players)):
                players[i].number = i+1
    
    def getTeamAverage(self):
        teamTotal = 0
        for i in self.team:
            teamTotal += i.getAverage()
        return teamTotal/len(self.team)

