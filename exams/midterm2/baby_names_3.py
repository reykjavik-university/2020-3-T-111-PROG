START_COL_FOR_BOYS = 1  # The starting column number for boys data (first column is 0)
START_COL_FOR_GIRLS = 3 # The staring column number for girls data

RANK_STRING = "50th percentile rank"

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

def split_lists(list_of_lists):
    '''Returns two lists based on list_of_lists, one for the boys, the other one for the girls.
    The ranking number in the first position of each inner list is removed'''
    boys = []
    girls = []
    for a_list in list_of_lists:
        boys.append(a_list[START_COL_FOR_BOYS:START_COL_FOR_BOYS+2])
        girls.append(a_list[START_COL_FOR_GIRLS:START_COL_FOR_GIRLS+2])
    
    return (boys, girls)

def compute_total_frequencey(names_freq_list):
    '''Returns the total frequency of names in the given list'''
    frequencies = [freq for name, freq in names_freq_list]
    return sum(frequencies)

def find_50_percent_rank(names_freq_list, total_frequency):
    '''Returns the ranks in the given list corresponding to >= 50% accumulated frequency of the total frequency''' 
    freq_accumulated = 0
    rank = 0
    fifty_percent_freq = 0.5 * total_frequency

    while freq_accumulated < fifty_percent_freq:
        rank += 1
        _, freq = names_freq_list[rank-1]
        freq_accumulated += freq
    
    return rank

def process_data(file_object):
    list_of_lines = get_baby_names_data(file_object)
    print(list_of_lines[:2])
    boys_freq_list, girls_freq_list = split_lists(list_of_lines)
    print(boys_freq_list[:5])
    print(girls_freq_list[:5])
    
    total_boys_freq = compute_total_frequencey(boys_freq_list)
    total_girls_freq = compute_total_frequencey(girls_freq_list)
    print("Total frequency of boy names:",total_boys_freq)
    print("Total frequency of girl names:",total_girls_freq)

    boys_50_percent_rank = find_50_percent_rank(boys_freq_list, total_boys_freq) 
    girls_50_percent_rank = find_50_percent_rank(girls_freq_list, total_girls_freq)   
    print(RANK_STRING + " for boys:",boys_50_percent_rank)
    print(RANK_STRING + " for girls:",girls_50_percent_rank)
 
# Main starts here
file_name = input("Enter file name: ")
file_object = open_file(file_name)
if not file_object:
    print("File {} not found".format(file_name))
else:
    process_data(file_object)