def battle(team, oppTeam):
    if(team.getTeamAverage() > oppTeam.getTeamAverage()):
        return "won"
    else:
        return "not won"
