def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None

def get_baby_names_data(file_object):
    '''Retrieves the data associated with the file object, converting number strings to ints.
    The data is returned as a list of lists, an inner list contains the tokens in each line.'''
    all_lines = []
    for line in file_object:
        token_list_from_line = line.strip().split()
        token_list_converted = [int(elem) if elem.isdigit() else elem for elem in token_list_from_line ]
        all_lines.append(token_list_converted)
    
    return all_lines


def process_data(file_object):
    list_of_lines = get_baby_names_data(file_object)
    print(list_of_lines[:2])
     
# Main starts here
file_name = input("Enter file name: ")
file_object = open_file(file_name)
if not file_object:
    print("File {} not found".format(file_name))
else:
    process_data(file_object)