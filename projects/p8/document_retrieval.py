import string

DOCUMENT_MARKER = '<NEW DOCUMENT>'
MENU_SEARCH = '1'
MENU_PRINT = '2'
MENU_QUIT = '3'
NO_MATCH_STR = "No match."

def open_file(filename):
    '''Opens the given filname and returns its file object, or None if not found'''
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None

def get_docs_list(file_object):
    '''Reads all documents in the file_object into a list and returns it.
    Each list entry is a string representing a document.'''

    all_docs = []
    doc = ''
    for line in file_object:
        # Store all lines of each document in string 
        # which is then appended to all_docs when a document marker is encountered
        if line.strip() == DOCUMENT_MARKER: 
            all_docs.append(doc)
            doc = '' # start new document
        else:
            doc += line
    else:   # Needed to handle the last document
        all_docs.append(doc)
    
    return all_docs
    

def build_dict(all_docs):
    '''Builds and returns a word dictionary for the given document list.
    The value of each word is a set of the document numbers the word appears in
    '''
    word_dict = {}

    for idx, doc_str in enumerate(all_docs): 
        word_list = doc_str.split()
        for word in word_list:
            word = word.strip().lower().strip(string.punctuation)
            if word:
                if word in word_dict:
                    word_dict[word].add(idx)
                else:
                    word_dict[word]={idx} # a set with one document number
    return word_dict

def get_document_set(word_dict,search_str):
    '''Returns a set of documents containing all the words in the search_str''' 
    search_list = search_str.strip().split()
    search_list = [word.lower() for word in search_list]
    document_set = set()

    if search_list:
        first_word = search_list[0]
        if first_word in word_dict:
            document_set = word_dict[first_word]
            # There might be more words in the search string
            for word in search_list[1:]:
                if word in word_dict:
                    document_set = document_set & word_dict[word]
                else:
                    document_set = set()
                    break
    return document_set

def get_action():
    ''' Reads the action as an integer from the user. If an error occurs, returns 3 '''
    
    def print_menu():
        print()
        print("What would you like to do?")
        print(f"{MENU_SEARCH}. Search Documents")
        print(f"{MENU_PRINT}. Print Document")
        print(f"{MENU_QUIT}. Quit Program")
    
    print_menu()
    action = input("> ")
    return action

def print_document_numbers(document_set):
    ''' Prints out document numbers, sorted in ascending order''' 
    document_list = sorted(document_set)
    if document_list:
        print("Documents that fit search:",end = ' ')
        for i in document_list:
            print(i, end = ' ')
        else:
            print()
    else:
        print(NO_MATCH_STR)

def print_document(all_docs, doc_num):
    '''Prints out the contents of a particular document. doc_num is zero-based'''
    if doc_num >= len(all_docs):
        print(NO_MATCH_STR)
    else:
        print("Document #{}".format(doc_num))
        print(all_docs[doc_num])

def execute_actions(all_docs, word_dict):
    action = get_action()
    while action in {MENU_SEARCH, MENU_PRINT}:
        if action == MENU_SEARCH:
            search_str = input("Enter search words: ")
            document_set = get_document_set(word_dict,search_str)
            print_document_numbers(document_set)
        elif action == MENU_PRINT:
            doc_num = int(input("Enter document number: "))
            print_document(all_docs, doc_num)
        action = get_action()
    else:
        print("Exiting program.")

# Main program starts here
document_file = input('Document collection: ')
file_object = open_file(document_file)
if file_object is not None:
    all_docs_list = get_docs_list(file_object)
    file_object.close()
    word_dict = build_dict(all_docs_list)
    execute_actions(all_docs_list, word_dict)
else:
    print("Documents not found.")