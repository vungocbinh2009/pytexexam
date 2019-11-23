import typing
from question import Question
import random


class Exam:
    def __init__(self, question_list: typing.List[Question]):
        self.question_list = question_list

    def shuffle_question(self):
        r = random.SystemRandom()
        r.shuffle(self.question_list)
