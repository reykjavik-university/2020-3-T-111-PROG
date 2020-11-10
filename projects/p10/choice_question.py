from question import Question

# A class that models multiple choice exam question
class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []

    def add_choice(self, choice, correct):
        '''Adds an answer choice to the question.
        correct is True if this is the correct choice, else False'''

        self._choices.append(choice)
        if correct:
            choice_str = str(len(self._choices))
            self.set_answer(choice_str)
    
    def __str__(self):
        result_str = super().__str__() + "\n"

        num_choices = len(self._choices)
        for i in range(num_choices):
            choice_no = i + 1
            result_str += "{}. {}".format(choice_no, self._choices[i])
            if i < num_choices - 1:
                result_str += "\n"
        return result_str

