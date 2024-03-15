from Team import Team

def battle(team: Team, oppTeam: Team):
    if(team.getTeamAverage() > oppTeam.getTeamAverage()):
        return "won"
    else:
        return "not won"
