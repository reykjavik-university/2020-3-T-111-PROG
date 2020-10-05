def unique_elements(a_list):
    ''' Returns a new list containing the unique elements in a_list '''
    result = []
    for elem in a_list:
        if not elem in result:
            result.append(elem)
    return result

def make_sorted_set(a_list):
    a_set = unique_elements(a_list)
    return sorted(a_set)

def intersection(set1, set2):
    result_set = []
    for elem in set1:
        if elem in set2:
            result_set.append(elem)
    return result_set

def union(set1, set2):
    result_list = set1 + set2
    result_set = make_sorted_set(result_list)
    return result_set

def get_set():
    a_list = input("Enter elements of a list separated by space: ").strip().split()
    a_list = [int(i) for i in a_list]
    return make_sorted_set(a_list)

# Main program starts here
set1 = get_set()
set2 = get_set()
print("Set 1: {}".format(set1))
print("Set 2: {}".format(set2))
set3 = intersection(set1, set2)
print("Intersection: {}".format(set3))
set4 = union(set1, set2)
print("Union: {}".format(set4))
