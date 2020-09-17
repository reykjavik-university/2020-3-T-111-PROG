def is_prime(num_int):
    '''Returns True if num_int is prime, otherwise False.'''
    for i in range(2,num_int):
        if num_int % i == 0:
            return False

    return True
    
max_num = int(input("Input an integer greater than 1: "))

for i in range (2, max_num+1): 
    if is_prime(i):
        print("{:d} is a prime".format(i))
    else:
        print("{:d} is not a prime".format(i))