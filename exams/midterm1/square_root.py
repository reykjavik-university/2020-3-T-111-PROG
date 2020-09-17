import math

# start_int = int(input("Input starting integer: "))
# square_root = math.sqrt(start_int)
# print(round(square_root,4))

# while square_root >= 2:
#     square_root = math.sqrt(square_root)
#     print(round(square_root,4))


# Einfaldari lausn
start_int = int(input("Input starting integer: "))

number_float = float(start_int)
while number_float >= 2:
    number_float = math.sqrt(number_float)
    print(round(number_float, 4))