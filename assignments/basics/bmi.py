weight_str = input("Weight (kg): ")
weight_float = float(weight_str)
height_str = input("Height (cm): ")
height_float = float(height_str) / 100

bmi = weight_float / height_float ** 2

print("BMI is: ", bmi)
