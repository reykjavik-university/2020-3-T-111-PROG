ISBN_LENGTH = 13    # Max length of the ISBN string
SEPARATOR = '-'  # The separator used
SEPARATOR_POS_LIST = [1,5,11] # The positions (indices) of the seprator
QUIT = 'q'

def read_isbn():
    ''' Reads and returns an ISBN string input from the user '''
    isbn_str = input("Enter an ISBN: ")
    return isbn_str.strip()

def separator_positions(a_str):
    ''' Returns true if the given string contains the SEPARATOR in the correct positions '''
    for pos in SEPARATOR_POS_LIST:
        if a_str[pos] != SEPARATOR:
            return False
    return True

def digit_sequences(a_str):
    ''' Returns true if the digits appear in correct positions in the given string '''
    for idx, char in enumerate(a_str):
        if not (char.isdigit() or idx in SEPARATOR_POS_LIST):
            return False  
    return True

def valid_format(isbn_str):
    ''' Returns true if the given ISBN string is valid, else false '''
    return len(isbn_str) == ISBN_LENGTH and separator_positions(isbn_str) and digit_sequences(isbn_str)

def analyse_isbn(isbn_str):
    ''' Prints an appropriate message depending on the validity of the ISBN string '''
    if not valid_format(isbn_str):
        print('Invalid format!')
    else:
        print("Valid format!")

# Main program starts here
if __name__ == "__main__":
    isbn_str = ''
    while isbn_str != QUIT:
        isbn_str = read_isbn()
        if isbn_str != QUIT:
            analyse_isbn(isbn_str)
