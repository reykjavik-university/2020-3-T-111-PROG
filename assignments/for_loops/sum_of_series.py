length = int(input("Input the length of series: "))

total = 0
sign = -1
for i in range(1, length+1):
    sign *= -1
    elem = sign*2*i
    total += elem
    print(elem)
print('Sum:',total) 
