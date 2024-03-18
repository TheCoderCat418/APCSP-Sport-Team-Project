from Team import Team
def levelUpPlayer(team: Team, playerNum: int, area, amt):
    match (area):
        case "strength":
            team.team[playerNum].setStrength(amt)
        case "communication":
            team.team[playerNum].setCommunication(amt)
        case "mood":
            team.team[playerNum].setMood(amt)
        case "agility":
            team.team[playerNum].setAgility(amt)
        case "reactionTime":
            team.team[playerNum].setReactionTime(amt)
        case "speed":
            team.team[playerNum].setSpeed(amt)
    return team