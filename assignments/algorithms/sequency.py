# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# The number n is entered by the user.  Each member of the sequence is written in a separate line.
# Implement the algorithm in Python.  Put your algorihmic description as a comment in the program file.

# Algorithm:
# Read the length of the sequence, n, from the user.
# Loop from 1 to n: 
# 
#   At step 1: set current = first = 1
#   At step 2: set current = second = 2
#   At step 3: set current = third = 3
#   At each step i > 3
#       add first, second and third to produce the current element
#       let first = second, second = third, third = current.
# 
#   print curent
#

n = int(input("Enter the length of the sequence: "))
for i in range(1, n+1):
    if i == 1:
        current = first = i
    elif i == 2:
        current = second = i
    elif i == 3:
        current = third = i
    else:
        current = first + second + third
        first, second, third = second, third, current
    print(current)

