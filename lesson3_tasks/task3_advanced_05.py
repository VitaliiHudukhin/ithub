import random

for i in range(10):
    rangeOfValues = [0,1,2]
    lst = []
    sumValue = 0
    helpValue = random.choice(rangeOfValues)
    while sumValue != 12:
        helpValue = random.choice(rangeOfValues)
        if sumValue+helpValue <= 12:
            sumValue+=helpValue
            lst.append(helpValue)
        else:
            pass
    print(*lst)

