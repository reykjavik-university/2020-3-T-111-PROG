def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def word_count_in_list(word_list):
    ''' Returns the number of words found in the specified list
        , . ! ? are considered separate words when appear at the end
        of a character sequence '''
    word_count = 0
    for word in word_list:
        if word[-1] in [',', '.', '!', '?']:
            word_count += 2
        else:
            word_count += 1
    return word_count

def get_word_count(file_stream):
    ''' Returns the number of words in the specified stream '''
    word_count = 0
    for line in file_stream:
        word_list = line.strip().split()
        word_count += word_count_in_list(word_list)
    return word_count

# Main program starts here
file_name = input("Enter filename: ")
file_stream = open_file(file_name)
if file_stream:
    word_count = get_word_count(file_stream)
    print(word_count)
    file_stream.close()
else:
    print("File {} not found!".format(file_name))