import string

def get_word_list(file_object):
    ''' Returns a list of the words found in the file assiciated with the file object
        The words are transformed to lower case and punctuation is stripped off the end of the word
    '''
    word_list = []
    for line in file_object:  
        line_lst = line.strip().split()
        for word in line_lst:
            word = word.lower()
            if word[-1] in string.punctuation:
                word = word[:-1]
            word_list.append(word)
    return word_list

def word_list_to_counts(word_list):
    '''Makes a dictionary of word counts from the given word list'''
    word_counts = {}

    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def dict_to_tuples(a_dict):
    '''Returns a list of tuples contains the key-value pairs in a_dict'''
    tuple_list = []
    for key, value in a_dict.items():
        a_tuple = (key,value)
        tuple_list.append(a_tuple)  
    return tuple_list


def main():
    filename = input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object) 
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    print(sorted(word_count_tuples))
    
main()