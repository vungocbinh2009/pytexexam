import random
from typing import List
from typing_extensions import Self

from pytexexam.component.component import Component, ShuffleableQuestion


class ComponentGroup(Component):
    """
    This class represents an group of components
    """
    def __init__(self, component_list: List[Component]):
        self.component_list = component_list
        """List of questions in the exam"""

    def shuffle_question(self, seed: int = None):
        """
        This method allows to shuffle all the questions order in the exam.
        :param seed: random seed
        """
        if seed is not None:
            random.seed(seed)
        random.shuffle(self.component_list)

    def shuffle_question_content(self, seed: int = None):
        """
        Shuffle all the content in each question, if a question is shuffleable
        :param seed:
        :return:
        """
        for comp in self.component_list:
            if comp is ShuffleableQuestion:
                comp: ShuffleableQuestion
                comp.shuffle_content(seed)

    def merge(self, group: Self):
        """Merge two question group into one"""
        self.component_list.extend(group)

    def split(self, index: int) -> tuple[Self, Self]:
        """
        Split question to two smaller question groups

        :param index: Index to split, that question will go to first group.
        :return:
        """
        group1 = self.component_list[:index]
        group2 = self.component_list[index:]
        return group1, group2

    def generate_exam(self) -> str:
        exam_code = ""
        for comp in self.component_list:
            exam_code += comp.generate_exam()
            exam_code += "\n\n"
        return exam_code

    def generate_answer(self) -> str:
        answer_code = ""
        for comp in self.component_list:
            answer_code += comp.generate_answer()
            answer_code += "\n\n"
        return answer_code

    def generate_solution(self) -> str:
        solution_code = ""
        for comp in self.component_list:
            solution_code += comp.generate_solution()
            solution_code += "\n\n"
        return solution_code
