MENU_INTERSECTION = '1'
MENU_UNION = '2'
MENU_DIFF = '3'
MENU_QUIT = '4'

def get_list():
    a_list = input("Input a list of integers separated with a comma: ").strip().split(",")
    a_list = [int(elem) for elem in a_list]
    return a_list

def get_operation():
    def print_menu():
        print(f"{MENU_INTERSECTION}. Intersection")
        print(f"{MENU_UNION}. Union")
        print(f"{MENU_DIFF}. Difference")
        print(f"{MENU_QUIT}. Quit")
    
    print_menu()
    operation = input("Set operation: ")
    return operation

def set_operations():
    oper = get_operation()
    
    while  oper in {MENU_INTERSECTION, MENU_UNION, MENU_DIFF}:
        if oper == MENU_INTERSECTION:
            new_set = set1 & set2
        elif oper == MENU_UNION:
            new_set = set1 | set2
        else:
            new_set = set1 - set2
        print(new_set)
        oper = get_operation()

# The main program starts here
list1 = get_list()
list2 = get_list()
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
set_operations()



