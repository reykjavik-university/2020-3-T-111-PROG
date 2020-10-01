import string

def find_unique(wordlist):
    unique = []
    
    for word in wordlist:
        if word not in unique:
            unique.append(word)
    return unique
    
def build_wordlist(filestream):
    all_words = []
    
    for line in filestream:
        words_in_line = line.strip().split()
        for word in words_in_line:
            word = word.strip(string.punctuation)
            all_words.append(word)
    return all_words
        
def main():
    filename = input("Enter filename: ")
    file_stream = open(filename)
    word_list = build_wordlist(file_stream)  
    file_stream.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()