# Accept d1 and d2, the number on two dices as input. 
# First, check to see that they are in the proper range for dice (1-6). If not, print the message "Invalid input". 
# If d1 and d2 have the same value, print out "Pair". Otherwise print the sum.

d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if d1 < 1 or d1 > 6 or d2 < 1 or d2 > 6:
    print("Invalid input")
else:
    if d1 == d2:
        print("Pair")
    else:
        print(d1+d2)