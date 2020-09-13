my_int = int(input('Give me an int >= 0: '))

if my_int == 0:
    bin_str = '0'
else:
    bin_str = ''
    quotient = my_int
    while quotient > 0:
        bin_str = str(quotient % 2) + bin_str
        quotient = quotient // 2
print("The binary of {} is {}".format(my_int,bin_str))