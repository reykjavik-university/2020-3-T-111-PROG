def sum_of_vectors(vector_list):
    '''Return a new list whose whose elements 
    are the sum of the corresponding elements in the vectors in vector_list'''

    # vector_list can be considered as a matrix.  Each element m_i_j then corresponds
    # to the element in row i, column j, in matrix m.
    # We need a double loop, because a matrix is two-dimensional
    sum_vector = []
    number_of_vectors = len(vector_list)
    length_of_vectors = len(vector_list[0]) 
    for i in range(length_of_vectors): 
        the_sum = 0
        # The inner loop sums over column no. i
        for j in range(number_of_vectors):
            the_sum += vector_list[j][i]    
        sum_vector.append(the_sum)
    return sum_vector

def convert_to_ints(vector_list):
    '''Converts all the elements of the nested vector_list to ints'''
    for vector in vector_list:
        for i, elem in enumerate(vector):
            vector[i] = int(elem)


def get_vectors(file_object):
    '''Reads a file containing the values of each vector in a separate line.
        Returns a list of the vectors '''
    vector_list = []
    for line in file_object:
        number_list = line.split()
        vector_list.append(number_list)
    return vector_list

def open_file(filename):
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None

# Main program starts here, DO NOT change
file_name = input("Enter filename: ")
file_object = open_file(file_name)
if file_object != None:
    vector_list = get_vectors(file_object)
    convert_to_ints(vector_list)
    print(vector_list)
    sum_vector = sum_of_vectors(vector_list)
    print(sum_vector)