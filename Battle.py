def battle(team, oppTeam):
    if(team.getTeamAverage() > oppTeam.getTeamAverage()):
        return "won", team.getTeamAverage() - oppTeam.getTeamAverage()
    else:
        return "not won", oppTeam.getTeamAverage() - team.getTeamAverage()
