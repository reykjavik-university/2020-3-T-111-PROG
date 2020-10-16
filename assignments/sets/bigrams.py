import string
import operator

MAX_BIGRAM_DISPLAY = 10

def open_file(filename):
    try:
        file_stream = open(filename, 'r')
        return file_stream
    except FileNotFoundError:
        return None

def get_word_list(file_stream):
    '''Reads the given stream and returns a list of lower case words.
    Punctuation at the start and end of a word are removed.'''
    all_words = []
       
    for line in file_stream:	
        line = line.strip()     # strip leading and trailing white space
        word_list = line.split() # get a list of words in the line
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation) # remove punctuation
            all_words.append(word)

    return all_words

def get_bigrams(word_list):
    ''' Creates a dictionary of bigrams from the given word_list.
        The keys are tuples of words that co-occur, the values are their occurances counts.
    '''
    bigrams = {}
    previous_word = ''
    for word in word_list:
        if previous_word != '':
            bigram = (previous_word, word)
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        previous_word = word
    return bigrams

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream is not None:
    all_words = get_word_list(file_stream)
    bigrams = get_bigrams(all_words)
    # First sort on the bigrams in alphabetical ordeer
    sorted_bigrams = sorted(bigrams.items())  
    # Then sort on the frequency in descending order
    sorted_bigrams = sorted(sorted_bigrams, key=operator.itemgetter(1), reverse=True)
    print(sorted_bigrams[:MAX_BIGRAM_DISPLAY])