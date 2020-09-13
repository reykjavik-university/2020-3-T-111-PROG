text_to_translate = input("Text to translate: ")

VOWELS = "aeiouyAEIOUY"
translation = ""

for word in text_to_translate.split():
    vowel_index = -1
    for index, character in enumerate(word):
        if character in VOWELS:
            vowel_index = index
            break
    if vowel_index == 0:
        translated_word = word + "yay"
    else:
        initial_consonents = word[:vowel_index]
        rest = word[vowel_index:]
        translated_word = rest + initial_consonents + "ay"
    translation += translated_word + " "

translation = translation.strip()  # get rid of trailing whitespace
print("Translation:", translation)