def open_file(filename):
    '''Opens the given file, returning its file object'''
    file_object = open(filename, 'r')
    return file_object

def write_tokens(file_object):
    '''Reads the given file, line by line, and write out the tokens from each line'''
    for sentence in file_object:	# process each line
        token = ''                  # initialize the token
        for char in sentence:
            if char.isspace():      # then we have reached the end of the current token
                print(token)
                token = ''          # clear the current token
            else:
                token += char

# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
write_tokens(file_object)
file_object.close()