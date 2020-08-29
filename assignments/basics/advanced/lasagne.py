# Advanced
degrees_f_str = input("Temperature in Fahrenheit: ")
degrees_f = int(degrees_f_str)
degrees_c = round((degrees_f - 32) * 5 / 9.0)
print("That's", degrees_c, "degrees Celcius")