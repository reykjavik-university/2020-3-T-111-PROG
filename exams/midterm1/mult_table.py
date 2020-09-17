number_to_multiply = int(input("Input number to multiply: "))
how_often = int(input("Input how often to multiply: "))

for i in range(1, how_often + 1):
    result = i * number_to_multiply
    print(result)

# Kannski ekki eins læsilegt en hugmyndaríkt
# for i in range(number_to_multiply, (how_often * number_to_multiply) + 1, number_to_multiply):
#    print(i)