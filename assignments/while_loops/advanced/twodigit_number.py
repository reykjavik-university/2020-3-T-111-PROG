num = 10

while num < 100:
    squared = num ** 2
    if squared < 1000:
        rightmost_two = squared % 100
        if rightmost_two == num:
            print(num)
    num += 1