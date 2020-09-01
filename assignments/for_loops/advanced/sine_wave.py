import math

number_of_cycles = float(input("Number of cycles: "))
number_of_lines = int(input("Stretched over how many lines? "))

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines
half_width = 20

for line in range(number_of_lines):
    radians = line * radians_per_line
    number_of_xs = round(half_width + math.sin(radians) * half_width)
    for i in range(number_of_xs):
        print("X", end="")
    print()
    
    # A shorter (and probably faster) method: 
    # print("X" * number_of_xs)
