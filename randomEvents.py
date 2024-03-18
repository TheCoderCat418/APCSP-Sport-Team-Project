from random import randint
def rollRandom(pot: int, winNums: int):
    luckyNum = randint(1, pot)
    randnums = []
    for i in range(winNums):
        while(True):
            num = randint(1, pot)
            for j in randnums:
                if(num == j):
                    continue
            break
    for i in randnums:
        if(i==luckyNum):
            return True
    return False


    