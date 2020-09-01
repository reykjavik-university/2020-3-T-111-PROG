max_num = int(input("Input maximum number: "))

for i in range(1, max_num+1):
    what_is_left = i
    sum_of_digits = 0
    while what_is_left > 0:
        last_digit = what_is_left % 10
        what_is_left = what_is_left // 10
        sum_of_digits += last_digit
    if sum_of_digits ** 3 == i:
        print(i) 