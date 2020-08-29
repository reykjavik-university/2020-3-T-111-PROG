n = int(input("Input a natural number: "))
potential_factor = 2

if n == 1:
    prime = False
else:
    prime = True

while potential_factor < n:
    if n % potential_factor == 0:
        prime = False
        break
    potential_factor += 1

if prime:
    print("Prime")
else:
    print("Not prime")