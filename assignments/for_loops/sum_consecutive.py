num = int(input("Input an int: ")) # Do not change this line

for i in range(1, num+1):
    sum = 0
    for j in range(1, i+1):
        sum += j
    print(sum)

