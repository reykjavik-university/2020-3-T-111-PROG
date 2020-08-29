a0 = int(input("Input a positive int: "))
x_n = a0
print(x_n)

while x_n > 1:
    if x_n % 2 == 0:    # Then x_n is even
        x_n = x_n // 2
    else:               # then x_n is odd
        x_n = 3*x_n + 1
    print(x_n)
