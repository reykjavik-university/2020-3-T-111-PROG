import math

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''Please choose one of the options below:
a. Display the sum of the first N natural numbers. 
b. Display the sum of the first N Fibonacci numbers. 
c. Display the approximate value of e using N terms.
x. Exit from the program.'''
       
    print(MENU)

def convert_to_valid_int(n_str):
    '''Converts the string n_str to an integer >= 2.
    Returns the corresponding integer or None if the string cannot be converted or the int is not valid'''
    if n_str.isdigit():
        n_int = int(n_str)
        if n_int >= 2:
            return n_int

    return None

def sum_natural(n_str):
    '''Computes the sum of the first n >= 2 natural numbers.'''
    n_int = convert_to_valid_int(n_str)
    if n_int == None:
        return None
    
    sum_int = 0
    for i in range(1, n_int + 1):
        sum_int += i
    return sum_int
    
def sum_fibonacci(n_str):
    '''Computes the sum of the first n >= 2 numbers in the Fibonacci series'''
    n_int = convert_to_valid_int(n_str)
    if n_int == None:
        return None
    
    first_number = 0
    second_number = 1
    sum_fibo = first_number + second_number
    
    for i in range(1, n_int - 1):
        next_number = first_number + second_number
        sum_fibo += next_number
        first_number = second_number
        second_number = next_number

    return sum_fibo

def approximate_euler(n_str):
    '''Computes the approximation of the Euler number using the first n_str >= 2 numbers in the series.'''

    NO_OF_SIGNIFICANT_DIGITS = 5
    n_int = convert_to_valid_int(n_str)
    if n_int == None:
        return None

    e = 0
    for i in range(0, n_int):
        term = 1/math.factorial(i)
        e += term
    return round(e, NO_OF_SIGNIFICANT_DIGITS)

def display_result(the_result, the_input, the_info_str):
    if the_result == None:
        print("Error: {} was not a valid number.".format(the_input)) 
    else:
        print("{}: {} ".format(the_info_str, the_result))
    
def main():

    display_options()
    option = input("\nEnter option: ")
    
    while option != 'x':
        if option == 'a' or option == 'b' or option == 'c':
            n_str = input("Enter N: ")

        if option == 'a':
            result = sum_natural(n_str)
            display_result(result, n_str, "Natural number sum")
            
        elif option == 'b':
            result = sum_fibonacci(n_str)
            display_result(result, n_str, "Fibonacci sum")
        
        elif option == 'c':
            result = approximate_euler(n_str)
            display_result(result, n_str, "Euler approximation")

        else:
            print("Unrecognized option {}".format(option))
            display_options()
            
        option = input("\nEnter option: ")

main()