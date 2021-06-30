while True:
    import random

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    die5 = random.randint(1,6)

    print(die1, die2, die3, die4, die5)

    if die1 == die2 and die2 == die3 and die3 == die4 and die4 == die5:
        print('Yatzee!')
        break
    else:
        print('Try again!')


