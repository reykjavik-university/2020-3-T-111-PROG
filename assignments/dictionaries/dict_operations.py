ADD = "a"
REMOVE = "r"
FIND = "f"

def add_to_dict(a_dict, key, value):
    ''' Adds the given key-value pair to a_dict '''
    if key in a_dict:
        return False
    else:
        a_dict[key] = value
        return True

def remove_from_dict(a_dict, key):
    ''' Remove the given key from a_dict '''
    try:
        a_dict.pop(key)
        return True
    except KeyError:
        return False

def find_key(a_dict, key):
    ''' Finds the value for the given key in a_dict'''
    try:
        value = a_dict[key]
        return value
    except KeyError:
        return None

def menu_selection():
    ''' Prompts for a menu selection '''
    print("Menu: ")
    choice = input("(a)dd, (r)emove, (f)ind: ").lower()
    return choice

def dict_to_tuples(a_dict):
    '''Returns a list of tuples contains the key-value pairs in a_dict'''
    tuple_list = []
    for key, value in a_dict.items():
        a_tuple = (key,value)
        tuple_list.append(a_tuple)  
    return tuple_list
    # Einfaldari lausn
    # return list(a_dict.items())

def execute_add(a_dict):
    key = input("Key: ")
    value = input("Value: ")
    success = add_to_dict(a_dict, key, value)
    if not success:
        print("Error. Key already exists.")

def execute_remove(a_dict):
    key = input("Key to remove: ")
    success = remove_from_dict(a_dict,key)
    if not success:
        print("Key not found.")

def execute_find(a_dict):
    key = input("Key to locate: ")
    value = find_key(a_dict,key)
    if not value is None:
        print("Value:", value)
    else:
        print("Key not found.")

def execute_selection(choice, a_dict):
    ''' Executes an operation on a_dict given the choice ''' 
    if choice == ADD:
        execute_add(a_dict)
    elif choice == REMOVE:
        execute_remove(a_dict)
    elif choice == FIND:
        execute_find(a_dict)
    else:
        print("Invalid choice.")

def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()