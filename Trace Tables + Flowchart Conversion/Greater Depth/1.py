Numbers = [45, 19, 62, 12]

for X in range(1, 4):
    Y = X - 1
    N = Numbers[X]
    while Y > -1 and N < Numbers[Y]:
        Numbers[Y + 1] = Numbers[Y]
        Y = Y - 1
    Numbers[Y + 1] = N
