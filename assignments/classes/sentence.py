class Sentence(object):
    def __init__(self, a_str = ''):
        self.sentence_string = a_str

    def get_first_word(self):
        words = self.sentence_string.split()
        return words[0]

    def get_all_words(self):
        return self.sentence_string.split()

    def replace(self,index,newWord):
        words = self.sentence_string.split()
        if 0 <= index < len(words):
            words[index] = newWord
            self.sentence_string = ' '.join(words)