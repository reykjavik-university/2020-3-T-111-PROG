DIGITS = 4

def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None
  
def get_data(file_object):
    '''Returns a list of strings found in each line in the given file_oject''' 
    str_list = []
    for a_str in file_object:
        str_list.append(a_str) 	
    return str_list

def get_floats(str_list):
    '''Returns a new list which contains only the float numbers from str_list'''
    num_list = []
    for a_str in str_list:
        try:
            float_num = float(a_str)
            num_list.append(float_num)
        except ValueError:
            continue
    return num_list

def get_cumulative_sums(num_list):
    '''Returns the cumulative sum in num_list, i.e. a sequence of partial sums'''
    cumulative_sum_list = []
    cumulative_sum = 0

    for num in num_list:
        cumulative_sum += num
        cumulative_sum_list.append(cumulative_sum)
    
    return cumulative_sum_list

def get_median(num_list):
    '''Returns the median of num_list'''
    if not num_list:
        return None

    sorted_num_list = sorted(num_list)
    length = len(sorted_num_list)
    middle_index = length // 2
    if length % 2 == 1:
        return sorted_num_list[middle_index]
    else:
        return (sorted_num_list[middle_index - 1] + sorted_num_list[middle_index]) / 2

def print_num_list(num_list):
    '''Prints the contents of num_list, in a single line with one space between the elements'''
    for num in num_list:
        print(round(num, DIGITS), end=' ')
    print()

def print_info_header(header_str):
    '''Prints a header string with leading \t and double \t in next linee'''
    print("\t"+header_str)
    print("\t\t", end='')

def process_one_file(file_object):
    '''Processes one file'''
    str_list = get_data(file_object)
    
    print_info_header("Sequence:")
    num_list = get_floats(str_list)
    print_num_list(num_list)
  
    print_info_header("Cumulative sum:")
    cumulative_sum_list = get_cumulative_sums(num_list)
    print_num_list(cumulative_sum_list)
  
    print_info_header("Sorted sequence:")
    print_num_list(sorted(num_list))
    
    print_info_header("Median:")
    median = get_median(num_list)
    if median != None:
        print(round(median, DIGITS))
    else:
        print()

def process_all_files(filename_list):
    '''Processes all the files in the given list'''
    for filename in filename_list:
        file_object = open_file(filename)
        if file_object != None:
            print("\nFile {}".format(filename))
            process_one_file(file_object)
            file_object.close()
        else:
            print("\nFile {} not found".format(filename))

# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)
