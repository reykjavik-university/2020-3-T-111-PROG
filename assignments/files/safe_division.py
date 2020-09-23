def divide_safe(num1_str, num2_str):
    '''Returns num1/num2 if the input is valid, else None'''
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        return num1/num2
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

# Do not change the lines below
num1_str = input('Input first number: ')
num2_str = input('Input second number: ')

result = divide_safe(num1_str, num2_str)
if result != None:
    print(round(result, 5))
else:
    print(result)
