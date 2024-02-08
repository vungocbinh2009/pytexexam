import random
from typing import List
from typing_extensions import Self

from pytexexam.component.component import Component, ShuffleableQuestion


class QuestionGroup(Component):
    """
    This class represents an exam.
    """
    def __init__(self, question_list: List[Component]):
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

    def shuffle_question_content(self, seed: int = None):
        for comp in self.question_list:
            if comp is ShuffleableQuestion:
                comp: ShuffleableQuestion
                comp.shuffle_content(seed)

    def merge(self, group: Self):
        self.question_list.extend(group)

    def split(self, index: int) -> tuple[Self, Self]:
        group1 = self.question_list[:index]
        group2 = self.question_list[index:]
        return group1, group2

    def generate_exam(self) -> str:
        exam_code = ""
        for comp in self.question_list:
            exam_code += comp.generate_exam()
            exam_code += "\n"
        return exam_code

    def generate_answer(self) -> str:
        answer_code = ""
        for comp in self.question_list:
            answer_code += comp.generate_answer()
            answer_code += "\n"
        return answer_code

    def generate_solution(self) -> str:
        solution_code = ""
        for comp in self.question_list:
            solution_code += comp.generate_solution()
            solution_code += "\n"
        return solution_code
