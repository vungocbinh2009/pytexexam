import typing
from question import Question


class Exam:
    def __init__(self, question_list: typing.List[Question]):
        self.question_list = question_list
