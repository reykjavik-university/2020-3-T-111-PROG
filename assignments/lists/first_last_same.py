def first_and_last_char_same(word_list):
    '''Returns a new list containing the words from word_list that begin and end with the same char'''
    result_list = []
    for word in word_list:
        if len(word) > 1 and word[0] == word[-1]:
            result_list.append(word)
    return result_list

def read_string():
    '''Prompts for an input string and returns it'''
    input_str = input('Enter word to be added to list: ')
    return input_str

def populate_list(a_list):
    '''Populates a_list with words until the user inputs "x"'''
    a_string = read_string()
    while a_string != 'x':
        a_list.append(a_string)
        a_string = read_string()

def print_list(a_list):
    for item in a_list:
        print(item)

# Main program starts here
initial_list = []
populate_list(initial_list)
print(initial_list)
new_list = first_and_last_char_same(initial_list)
print_list(new_list)
