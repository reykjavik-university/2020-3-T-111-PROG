from question import Question
from choice_question import ChoiceQuestion

class Exam():
    def __init__(self):
        '''Initializes a list of Questions and ChoiceQuestions, and total points'''
        self.__question_list = []
        self.__choice_question_list = []
        self.__points = 0

    def __get_answer(self):
        response = input("Your answer: ")
        return response
    
    def __update_points(self, question, answer):
        if question.check_answer(answer):
            self.__points += 1

    def __present_question(self, question):
        '''Presents the question and allows the user to answer it'''
        print(question)
        answer = self.__get_answer()
        print(question.check_answer(answer))
        self.__update_points(question, answer)
        print()

    def get_points(self):
        return self.__points

    def get_num_questions(self):
        return len(self.__question_list) + len(self.__choice_question_list)

    def add_question(self, question_str, answer_str):
        '''Adds an instance of Question to the exam'''
        question = Question()
        question.set_question(question_str)
        question.set_answer(answer_str)

        self.__question_list.append(question)

    def add_choice_question(self, question_str, choice_list):
        '''Adds an instance of ChoiceQuestion to the exam. 
        choice_list is a list of tuples (str, bool), where the first part is a choice and the second part is a bool indicating true or false'''
        question = ChoiceQuestion()
        question.set_question(question_str)
        for choice_tuple in choice_list:
            question.add_choice(choice_tuple[0], choice_tuple[1])
        
        self.__choice_question_list.append(question)
    
    def present_exam(self):
        '''First present the Question questions and then the ChoiceQuestion questions'''
        for question in self.__question_list:
            self.__present_question(question)
            
        for question in self.__choice_question_list:
            self.__present_question(question)
