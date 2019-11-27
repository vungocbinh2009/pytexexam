from answer import Answer
import random
from typing import Dict


class Question:
    """
    This class represents one question on the test.
    """
    def __init__(self, question: str):
        self.question: str = question
        """Content of the question."""
        self.__answer_a = Answer()
        """Content of the answer A"""
        self.__answer_b = Answer()
        """Content of the answer B"""
        self.__answer_c = Answer()
        """Content of the answer C"""
        self.__answer_d = Answer()
        """Content of the answer D"""
        self.__answer_column = 1
        """Number of columns for which the answer will be presented. Answers can be presented as 
        1 column, 2 columns or 4 columns"""
        self.__solution = ""
        """Solution of the question"""

    def answer_a(self, answer: str, true_answer=False):
        """
        This method is used to enter answer A for the question.

        :param answer: Content of the answer A
        :param true_answer: If this is the correct answer then enter True, if false then enter
        False.
        """
        self.__answer_a.answer = answer
        self.__answer_a.is_true_answer = true_answer

    def answer_b(self, answer: str, true_answer=False):
        """
        This method is used to enter answer B to the question.

        :param answer: Content of the answer B
        :param true_answer: If this is the correct answer then enter True, if false then enter
        False.

        """
        self.__answer_b.answer = answer
        self.__answer_b.is_true_answer = true_answer

    def answer_c(self, answer: str, true_answer=False):
        """
        This method is used to enter answer C to the question.

        :param answer: Content of the answer C
        :param true_answer: If this is the correct answer then enter True, if false then enter
        False.

        """
        self.__answer_c.answer = answer
        self.__answer_c.is_true_answer = true_answer

    def answer_d(self, answer: str, true_answer=False):
        """
        This method is used to enter answer D for the question.

        :param answer: Content of the answer D
        :param true_answer: If this is the correct answer then enter True, if false then enter
        False.

        """
        self.__answer_d.answer = answer
        self.__answer_d.is_true_answer = true_answer

    def answers(self, true_answer: str, answer_dict: Dict[str, str]):
        """
        Another way to enter answers to questions.

        :param true_answer: The letter that corresponds to the correct answer in the question (A, B, C, D)
        :param answer_dict: A dictionary contains the answers to the questions.The corresponding
        key of this dictionary is A, B, C, D.
        """
        self.__answer_a.answer = answer_dict.get("A")
        self.__answer_b.answer = answer_dict.get("B")
        self.__answer_c.answer = answer_dict.get("C")
        self.__answer_d.answer = answer_dict.get("D")
        if true_answer == "A":
            self.__answer_a.is_true_answer = True
        elif true_answer == "B":
            self.__answer_b.is_true_answer = True
        elif true_answer == "C":
            self.__answer_c.is_true_answer = True
        else:
            self.__answer_d.is_true_answer = True

    def get_answer(self, answer_number: int) -> str:
        """
        This method is used to get answers to questions.

        :param answer_number: The number corresponding to the answer of the question.
        Specifically: want to get answer A then enter 1, B enter 2, C enter 3, and D enter 4.
        :return: The answer corresponds to the selected answer.

        """
        answer_list = {
            1: self.__answer_a.answer,
            2: self.__answer_b.answer,
            3: self.__answer_c.answer,
            4: self.__answer_d.answer
        }
        return answer_list.get(answer_number, "Invalid")

    def shuffle_answer(self):
        """
        The method that allows the swap answers in question.

        """
        answer_list = [self.__answer_a, self.__answer_b, self.__answer_c, self.__answer_d]
        r = random.SystemRandom()
        r.shuffle(answer_list)
        self.__answer_a = answer_list[0]
        self.__answer_b = answer_list[1]
        self.__answer_c = answer_list[2]
        self.__answer_d = answer_list[3]

    def set_answer_column(self, answer_column: int):
        """
        This method allows you to enter the number of columns where the answer will be displayed
        when printing the question. The possible values ​​are 1, 2, 4

        :param answer_column: The number of columns the answer will be displayed when printed.

        """
        if answer_column in [1, 2, 4]:
            self.__answer_column = answer_column

    def get_answer_column(self) -> int:
        """
        This method returns the number of columns where the answer will be presented when the
        question is printed. The function can return 1, 2, 4.

        :return: The number of columns the answer will be displayed when the question is printed
        """
        return self.__answer_column

    def get_true_answer(self) -> str:
        """
        This method returns the character corresponding to the correct answer of the question.
        The possible answer are A, B, C, D.

        :return: The letter corresponding to the correct answer of the question
        """
        if self.__answer_a.is_true_answer:
            return "A"
        elif self.__answer_b.is_true_answer:
            return "B"
        elif self.__answer_c.is_true_answer:
            return "C"
        else:
            return "D"

    def solution(self, solution: str):
        """This method is used to enter detailed answer to the question"""
        self.__solution = solution

    def get_solution(self) -> str:
        return self.__solution
