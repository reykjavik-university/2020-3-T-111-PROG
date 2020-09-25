import string

def get_chars_as_list(sentence):
	char_list = []
	for ch in sentence:
		char_list.append(ch)
	return char_list

# main program starts here
sentence = input("Input a sentence: ")
#char_list = get_chars_as_list(sentence)
char_list = list(sentence)
print(char_list)
char_list.sort()
print(char_list)