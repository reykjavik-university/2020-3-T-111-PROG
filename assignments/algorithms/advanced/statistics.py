import math

# The formulas that we leverage can be found here:
# https://en.wikipedia.org/wiki/standard_deviation#Rapid_calculation_methods

previous_average = 0
previous_q = 0
number_count = 0

while True:
    x = int(input("Enter a number (-1 to exit) "))
    if x == -1:
        break

    number_count += 1

    # Update the cumulative moving average (CMA)
    current_average = previous_average + (x - previous_average) / number_count

    # Update the running standard deviation
    current_q = previous_q + (x - previous_average) * (x - current_average)
    population_variance = current_q / number_count
    standard_deviation = math.sqrt(population_variance)

    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))

    # Store the values from the current iteration so that we can use them in
    # the next one
    previous_average = current_average
    previous_q = current_q
