n = int(input("Input an int: "))
count = 1

while count <= n:
    if n%count == 0:
        print(count)
    count += 1