# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A



def scoresAndGrades(i):
    for num in range(0,10):
        import random
        num = random.randint(60, 101)
        i -= 1
        if num <= 69:
            print "Score:", num, "; Your grade is D"
        elif num<=79:
            print "Score:", num, "; Your grade is C"
        elif num<=89:
            print "Score:", num, "; Your grade is B"
        elif num<=101: 
            print "Score:", num, "; Your grade is A"
scoresAndGrades(10)


