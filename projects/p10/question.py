# A class that models exam question
class Question:
    def __init__(self):
        '''Constructs an instance with an empty question and an empty answer'''
        self._question_str = ''
        self._answer_str = ''

    def set_question(self, question_str):
        self._question_str = question_str
    
    def set_answer(self, answer_str):
        self._answer_str = answer_str
    
    def check_answer(self, response):
        return response.lower() == self._answer_str.lower()
    
    def __str__(self):
        return self._question_str
    
    def __repr__(self):
        return "Q: {} A: {}".format(self._question_str, self._answer_str)
