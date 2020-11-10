MENU_SUM = 1
MENU_PRODUCT = 2
MENU_QUIT = 9
MENU_PERFORMERS = [MENU_SUM, MENU_PRODUCT]
MENU_PROMPT = '{}: Compute the sum of 1..n\n{}: Compute the product of 1..n\n{}: Quit\nChoice: '.format(MENU_SUM, MENU_PRODUCT, MENU_QUIT)

def get_int_input(a_prompt):
    try:
        choice = int(input(a_prompt))
        return choice
    except ValueError:
        return None

def compute_sum(n_int):
    the_sum = 0
    for i in range(1, n_int + 1):
        the_sum += i

    return the_sum

def compute_product(n_int):
    the_product = 1
    for i in range (1, n_int + 1):
        the_product *= i
    
    return the_product

def perform_menu_action(choice, n_int):
    if choice == MENU_SUM:
        the_result = compute_sum(n_int)
    elif choice == MENU_PRODUCT:
        the_result = compute_product(n_int) 
    print('The result is: {}'.format(the_result))    

# Main starts here
choice = get_int_input(MENU_PROMPT)
while choice != MENU_QUIT:
    if choice in MENU_PERFORMERS:
        n_int = get_int_input("Enter value for n: ")
        if n_int is not None:
            perform_menu_action(choice, n_int)    
    choice = get_int_input(MENU_PROMPT)
    