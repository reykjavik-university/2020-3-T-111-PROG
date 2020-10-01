def remove_evens(int_list):
    '''Removes even integers from int_list'''
    a_copy = int_list[:]
    for num in a_copy:
        if num % 2 == 0:
            int_list.remove(num)

def remove_evens2(int_list):
    '''Returns a new list with only odd integers from int_list'''
    return [num for num in int_list if num % 2 != 0]

# Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)