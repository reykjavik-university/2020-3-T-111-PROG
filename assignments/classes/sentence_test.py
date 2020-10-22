from sentence import Sentence

sent = Sentence('This is a test')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(3, "must")
print(sent.get_all_words())