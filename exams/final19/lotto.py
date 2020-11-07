MIN = 1
MAX = 40
COUNT_OF_NUM = 5

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def valid_range(number_list):
    ''' Returns true if all numbers in the given list are within the range '''
    for num in number_list:
        if num < MIN or num > MAX:
            return False
    return True

def convert_to_ints(str_list):
    ''' Converts the list of strings to a list of ints.
        Returns None if the list of strings is not valid. '''
    try:
        number_list = [ int(i) for i in str_list]
        return number_list
    except ValueError:
        return None

def get_winning_numbers():
    ''' Returns a list of the winning numbers entered by the user.
        Return None if the numbers entered are not valid. '''
    numbers_str = input("Enter winning numbers: ").split()
    num_list = convert_to_ints(numbers_str)

    if num_list:
    # Valid winning row?
        num_set = set(num_list)
        if len(num_set) != COUNT_OF_NUM or not valid_range(num_list):        
            return None
    
    return num_list
    
def read_lotto_rows(file_object):
    ''' Returns lotto rows from file stream and returns them as list of lists '''
    lotto_rows = []
    for line in file_object:
        str_list = line.strip().split()
        int_list = convert_to_ints(str_list)
        lotto_rows.append(int_list)
    return lotto_rows

def print_correct_numbers(winning_numbers_list, lotto_rows_list):
    ''' Finds and prints the correct numbers in each lotto row, given the winning numbers.
        A correct number is marked with an asterisk'''
    for lotto_row in lotto_rows_list:
        for num in lotto_row:
            if num in winning_numbers_list:
                print("{}*".format(num),end=' ')
            else:
                print(num,end=' ')
        print()

def read_data_and_compare(file_object):
    ''' Reads file data, winnings numbers and compares '''
    winning_numbers_list = get_winning_numbers()
    if winning_numbers_list:
        lotto_rows_list = read_lotto_rows(file_object)
        print_correct_numbers(winning_numbers_list, lotto_rows_list)
    else:
        print("Winning numbers are invalid!")

# Main program starts here
if __name__ == "__main__":
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    if file_object:
        read_data_and_compare(file_object)
    else:
        print("File {} not found!".format(file_name))
