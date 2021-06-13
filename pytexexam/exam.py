import random
from typing import List

from question import Question


class Exam:
    """
    This class represents an exam.
    """
    def __init__(self, question_list: List[Question]):
        self.question_list = question_list
        """List of questions in the exam"""

    def shuffle_question(self, seed: int = None):
        """
        This method allows to shuffle all the questions in the exam.
        :param seed: random seed
        """
        if seed is not None:
            random.seed(seed)
        random.shuffle(self.question_list)
