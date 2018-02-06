import random

def coin(i):
    headcount = 0
    tailcount = 0
    for num in range(i):
        randomnum = random.randint(1,2)
        if randomnum == 1:
            headcount +=1
            print 'Attempt #', i, 'It is a head. You have', headcount, 'head(s).'
        elif randomnum == 2:
            tailcount += 1
            print 'Attempt #', i, 'It is a tail. You have', tailcount, 'tail(s).'
        i -= 1
coin(5000)
   


