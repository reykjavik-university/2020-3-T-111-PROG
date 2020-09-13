a_str = input("Input a string: ")

inside_word = False
no_of_words = 0
no_of_letters = 0

for char in a_str:
    if char.isalpha() or char.isdigit():
        no_of_letters += 1
        if not inside_word:
            no_of_words += 1
        inside_word = True
    else:
        inside_word = False

print("No. of letters {}, no. of words: {}".format(no_of_letters, no_of_words))
