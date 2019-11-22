import typing
from answer import Answer


class Question:
    def __init__(self, question: str):
        self.question: str = question
        self.answer_list: typing.List[Answer] = []

    def add_answer(self, answer: str, is_true_answer=False):
        answer_obj = Answer(answer, is_true_answer)
        self.answer_list.append(answer_obj)
        return self
