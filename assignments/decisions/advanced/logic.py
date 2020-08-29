# Advanced
a = bool(int(input("A")))
b = bool(int(input("B")))
c = bool(int(input("C")))

d = int((a and (not b)) or ((not a) and c))

print("D is", d)