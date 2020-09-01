max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

days_when_amount_aquired = 0
amount = 0

for i in range(0, max_days):
    amount += 2**i
    if amount >= target:
        days_when_amount_aquired = i+1
        break

print('Days needed:',days_when_amount_aquired)
