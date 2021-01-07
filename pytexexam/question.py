import string
from random import SystemRandom

from .answer import Answer
from typing import List


class Question:
    """
    This class represents one question on the test.
    """
    def __init__(self, question: str, answers: List[str], true_answer: str, solution: str, answer_column: int):
        self.question: str = question
        """Content of the question."""
        self.answers: List[Answer] = self.__get_answer_list(answers, true_answer)
        """Question answers"""
        self.answer_column = answer_column
        """Number of columns for which the answer will be presented."""
        self.solution = solution
        """Solution of the question"""

    @staticmethod
    def __get_answer_list(answers: List[str], true_answer: str) -> List[Answer]:
        """
        Generate a list of answer object from answer and true answer key
        :param answers: question answer list.
        :param true_answer: answer key of true answer.
        :return: a list of answer object.
        """
        answer_key = Question.__get_answer_key()
        answer_list_size = min(len(answer_key), len(answers))
        answer_list: List[Answer] = []
        for i in range(0, answer_list_size):
            answer_list.append(Answer(answer_key[i], answers[i], answer_key[i] == true_answer))
        return answer_list

    @staticmethod
    def __get_answer_key() -> List[str]:
        """
        get list of alphabet character. (to use it as answer key)
        :return: Alphabet character list.
        """
        return list(string.ascii_uppercase)

    def shuffle_answer(self):
        SystemRandom().shuffle(self.answers)
