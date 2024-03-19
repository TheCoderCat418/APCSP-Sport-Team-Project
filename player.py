from random import randint


class Player:
    def __init__(
        self,
        commmunication: int,
        reactionTime: int,
        speed: int,
        strength: int,
        agility: int,
        mood: int,
    ):
        self.communication = commmunication
        self.reactionTime = reactionTime
        self.speed = speed
        self.name = "Unnamed"
        self.strength = strength
        self.agility = agility
        self.mood = mood

    def getCommunication(self) -> int:
        return self.communication

    def getMood(self) -> int:
        return self.mood

    def getReactionTime(self) -> int:
        return self.reactionTime

    def getSpeed(self) -> int:
        return self.speed

    def getAgility(self) -> int:
        return self.agility

    def getStrength(self) -> int:
        return self.strength

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setMood(self, mood):
        self.mood = mood

    def setCommunication(self, communication):
        self.communication = communication

    def setReactionTime(self, reactionTime):
        self.reactionTime = reactionTime

    def setSpeed(self, speed):
        self.speed = speed

    def setAgility(self, agility):
        self.agility = agility

    def setStrength(self, strength):
        self.strength = strength

    def getAverage(self):
        total = 0
        total += self.getAgility()
        total += self.getMood()
        total += self.getCommunication()
        total += self.getReactionTime()
        total += self.getSpeed()
        total += self.getStrength()
        return total / 6


def makeRandomPlayer() -> Player:
    return Player(
        randint(1, 100),
        randint(1, 100),
        randint(1, 100),
        randint(1, 100),
        randint(1, 100),
        randint(1, 100),
    )
