import typing
from answer import Answer


class Question:
    def __init__(self, question: str):
        self.question: str = question
        self.answer_1 = Answer()
        self.answer_2 = Answer()
        self.answer_3 = Answer()
        self.answer_4 = Answer()

    