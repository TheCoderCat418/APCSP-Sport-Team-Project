from random import randint


def rollRandom(pot: int, winNums: int):
    luckyNum = randint(0, pot)
    randnums = []
    for i in range(pot):
        randnums.append(i)

    for i in range(winNums):
        if randnums[randint(0, pot-1)] == luckyNum:
            return True
    return False
