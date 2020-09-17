def every_other_chr(a_str):
    '''Returns a new string containing every other character in a_str.'''
    return a_str[::2]
    
input_str = input("Enter a string: ")

print("Every other character:", every_other_chr(input_str))
