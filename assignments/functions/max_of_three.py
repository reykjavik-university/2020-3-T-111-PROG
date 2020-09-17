def max_of_two(x,y):
    if x > y:
        return x
    return y

def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
    
maximum = max_of_three(first, second, third)