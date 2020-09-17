max_int = int(input("Input max integer: "))

for i in range(1, max_int+1):
    for j in range (1, i+1):
        print(j, end=' ')
    print()
