class StringSet:
    
    def __init__(self, a_string=''):
        self.__words = []
        for word in a_string.split():
            self.add(word)
            
    def __str__(self):
        return " ".join(self.__words)

    def add(self, word):    
        if word not in self.__words:
            self.__words.append(word)
    
    def __add__(self, other):
        result = StringSet()
        for word in self.__words:
            result.add(word)
        for word in other.__words:
            result.add(word)

        return result

    def size(self):
        return len(self.__words)

    def at(self, index):
        return self.__words[index]

    def find(self, word):
        return word in self.__words


