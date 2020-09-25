import string

def get_unique_letters(sentence):
	unique_letters = []
	for ch in sentence:
		if ch not in string.punctuation and ch not in string.whitespace and ch not in unique_letters:
			unique_letters.append(ch)
	return unique_letters

# main program starts here
sentence = input("Input a sentence: ")
unique_letters = get_unique_letters(sentence)
print("Unique letters:", unique_letters)
