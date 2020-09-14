choice = input("Input f|a|b (fibonacci, abundant or both): ")

# In the Fibonacci sequence, the first two numbers are 0 and 1, but thereafter each number in the sequence is the sum of the two previous numbers.
if choice == 'f' or choice == 'b':
    # Fibonacci Sequence
    max_len = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")

    first_number = 0
    second_number = 1
    print(first_number)
    print(second_number)

    for i in range(1, max_len - 1):
        next_number = first_number + second_number
        print(next_number)
        first_number = second_number
        second_number = next_number

# Abundant number
# In number theory, an abundant number is a number for which the sum of its proper divisors is greater than the number itself. 
# The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16.
if (choice == 'a' or choice == 'b'):
    max_number = int(input("Input the max number to check: "))

    print("Abundant numbers:")
    print("-----------------")

    for potential_abundant in range(1, max_number+1):
        sum_divisors = 0
        for potential_divisor in range(1, potential_abundant):
            if potential_abundant % potential_divisor == 0: 
                sum_divisors += potential_divisor
        if sum_divisors > potential_abundant:
            print(potential_abundant)