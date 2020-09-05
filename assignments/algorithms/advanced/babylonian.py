# Gather input from the user
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

count = 0  # count the number of guesses
previous = 0  # track the previous calculated value

# Until we are within tolerance, keep inching our way towards the square root
while abs(previous - guess) > tolerance:
    previous = guess
    quotient = number / guess
    guess = (quotient + guess) / 2
    count += 1

print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")
