days = [10, 15, 4]
sales = [20, 33, 12]
weeks = [0, 0, 0]

for i in range(3):
    daysTotal = days[i] + sales[i]
    weeks[i] = daysTotal // 7

weeksTotal = weeks[0] + weeks[1] + weeks[2]
print(weeksTotal)
