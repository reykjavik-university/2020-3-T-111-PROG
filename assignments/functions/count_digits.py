def count_digits(a_str):
    '''Returns the count of digits in a_str.'''
    count = 0
    for ch in a_str:
        if ch.isdigit():
            count += 1
    
    return count

input_str = input("Enter a string: ")

digit_count = count_digits(input_str)
print("No. of digits:", digit_count)
