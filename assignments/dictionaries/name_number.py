def get_name_number_pair():
    '''Returns a tuple of name and number entered by the user'''
    name = input("Name: ")
    number = input("Number: ")
    return (name, number)

def dict_to_tuples(a_dict):
    '''Returns a list of tuples contains the key-value pairs in a_dict'''
    tuple_list = []
    for key, value in a_dict.items():
        a_tuple = (key,value)
        tuple_list.append(a_tuple)  
    return tuple_list

def more_data():
    more = input('More data (y/n)? ')
    return more.lower() == 'y'

# Main program starts here
name_number_dict = {}

go_again = True
while go_again:
    name, number = get_name_number_pair()
    name_number_dict[name] = number
    go_again = more_data()

tuple_list = dict_to_tuples(name_number_dict)     
print(sorted(tuple_list))