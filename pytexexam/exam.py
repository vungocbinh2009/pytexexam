from random import SystemRandom
from typing import List

from question import Question


class Exam:
    """
    This class represents an exam.
    """
    def __init__(self, question_list: List[Question]):
        self.question_list = question_list
        """List of questions in the exam"""

    def shuffle_question(self):
        """
        This method allows to shuffle all the questions in the exam.
        """
        SystemRandom().shuffle(self.question_list)
