def check_consecutive(user_list, num_to_check): 
    for i in range(len(user_list)-1):
        if user_list[i] == num_to_check == user_list[i+1]:
            return True 
    return False

def get_list():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    try:
        a_list = [int(elements) for elements in a_list]
        return a_list
    except ValueError: 
        return None

def main():
    a_list = get_list()
    if a_list:
        potential_consecutive = int(input("Consecutive check: "))
        result = check_consecutive(a_list, potential_consecutive)
        print(result)
    else: 
        print("Error: enter only integers.")

main()