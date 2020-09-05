# Algorithm:
# Assume that the maximum number read so far is max_int = 0.
# Repeatedly ask the user to input a number, num_int, until she inputs a negative number.
#   At each step during the loop: If num_int is greater then max_int then max_int gets the value of num_int.
# Finally, print out max_int.

max_int = 0

num_int = int(input("Input a number: "))    # Do not change this line
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line
