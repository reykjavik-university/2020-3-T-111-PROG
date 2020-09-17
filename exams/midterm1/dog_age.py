dog_age = int(input("Input dog's age: ")) # Do not change this line

if dog_age < 1 or dog_age > 16:
    print("Invalid age")
else:
    if dog_age >= 2:
        years_more_than_2 = dog_age - 2
        human_age = 24 + 4 * years_more_than_2
    else:
        human_age = 15
    print("Human age:", human_age)  