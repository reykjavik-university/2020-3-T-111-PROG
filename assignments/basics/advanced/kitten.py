# Advanced
r_0_str = input("What's the basic reproduction rate (R_0)? ")
r_0 = float(r_0_str)
total_cases = 1 + r_0 + r_0 ** 2 + r_0 ** 3
print("Total cases after 3 rounds of transmission:", round(total_cases))