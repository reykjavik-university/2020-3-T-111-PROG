num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

min_int = num1
if num2 < min_int:
    min_int = num2
if num3 < min_int:
    min_int = num3

print("The minimum is: ", min_int) # Do not change this line