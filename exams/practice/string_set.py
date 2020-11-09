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


def main():
    str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
    set1 = StringSet(str1)
    str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
    set2 = StringSet(str2)
    print("Set1:", set1)
    print("Set2:", set2)
    print("Set1 size:", set1.size())
    print("Set2 size:", set2.size())
    the_union = set1 + set2
    print("Union:", the_union)
    print("Union size:", the_union.size())

    query = StringSet('chocolate cream fish good rubbish')
    print("Query:", query)
    count = 0
    for i in range(query.size()):
        if the_union.find(query.at(i)):
            count += 1
    
    print("Query size:", query.size())
    print("Found in union:", count)

main()