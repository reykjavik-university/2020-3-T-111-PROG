def common_letters_list(first_str, last_str):
    '''Return a list of common letters in first_str and last_str.'''
    common = []

    for ch in first_str:
        if ch in last_str and ch not in common:
            common.append(ch)

    return common

def common_letters_set(first_str, last_str):
    '''Return a set of common letters in first_str and last_str.'''
    set1 = set(first_str)
    set2 = set(last_str)
    return set1 & set2

# Main program starts here
name = input("Enter name: ").lower()
first, last = name.split()
common_list = common_letters_list(first, last)
common_set = common_letters_set(first, last)
print(sorted(common_list))
print(sorted(common_set))

