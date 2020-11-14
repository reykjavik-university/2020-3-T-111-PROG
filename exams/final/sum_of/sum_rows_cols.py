def open_file(file_name):
    '''Opens the given filname and returns its file object, or None if not found'''
    try:
        file_object = open(file_name, 'r')
        return file_object
    except FileNotFoundError:
        return None

def read_matrix(file_object):
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    matrix = []
    for line in file_object:
        row_str = line.split()
        row_int = [int(number) for number in row_str]
        matrix.append(row_int)
    
    return matrix
    
def display(matrix):
    '''Display the matrix, printing it one row in each line'''
    dimension = len(matrix)
    for i in range(dimension):
        for j in range(dimension):
            print(matrix[i][j], end="\t")
        print()    

def row_sum_same(matrix):
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    last_sum = 0
    first_row = True

    for row in matrix:
        sum_row = sum(row)
        if first_row:
            first_row = False
        elif sum_row != last_sum:
            return 0
        last_sum = sum_row
    
    return last_sum

def col_sum_same(matrix):
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    dimension = len(matrix)
    last_sum = 0
    first_col = True
    
    for i in range(dimension):
        sum_col = 0
        for j in range(dimension):
            sum_col += matrix[j][i]
        if first_col:
            first_col = False
        elif sum_col != last_sum:
            return 0
        last_sum = sum_col
    
    return sum_col

def is_same_sums(matrix):
    '''Returns true if the sum of the elements in each row and each colunm of the matrix is the same value'''
    return 0 != row_sum_same(matrix) == col_sum_same(matrix)

def main():
    file_name = input("File name: ")
    file_object = open_file(file_name)
    if file_object is None:
        print("File not found")
    else:
        matrix = read_matrix(file_object)
        file_object.close()
        display(matrix)
        same_sums = is_same_sums(matrix)
        if same_sums:
            print("Same sums")
        else:
            print("Not same sums")

# Main program starts here
if __name__ == "__main__":
    main()