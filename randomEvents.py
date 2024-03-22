from random import randint


def rollRandom(pot: int, winNums: int):
    luckyNum = randint(0, pot-1)
    potArr = []
    for i in range(pot):
        potArr.append(i)
    for i in range(winNums):
        if potArr[randint(0, pot-1)] == luckyNum:
            return True
    return False

