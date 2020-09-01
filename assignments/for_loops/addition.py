first = int(input("Input the first integer: "))
second = int(input("Input the second integer: "))

product = 0
for i in range(1, second+1):
	product += first

print(product)