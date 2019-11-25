import typing
from question import Question
import random


class Exam:
    """
    This class represents an exam.
    """
    def __init__(self, question_list: typing.List[Question]):
        self.question_list = question_list
        """List of questions in the exam"""

    def shuffle_question(self):
        """
        This method allows to shuffle all the questions in the exam.
        """
        r = random.SystemRandom()
        r.shuffle(self.question_list)
