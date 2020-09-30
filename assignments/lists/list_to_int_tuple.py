def list_to_int_tuple(a_list):
    int_list = []
    for item in a_list:
        try:
            int_item = int(item)
            int_list.append(int_item)
        except ValueError:
            continue
    return tuple(int_list)

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_int_tuple(a_list)
print(a_tuple)