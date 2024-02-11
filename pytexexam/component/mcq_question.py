import random

from pytexexam.component.component import Component, ShuffleableQuestion
from pytexexam.jinja2env import jinja_env
from pytexexam.latex_util.internal import get_answer_key


class MultipleChoiceAnswer:
    """
    This class is used to store 1 answer in a question.
    """

    def __init__(self, answer_key: str, answer: str, is_true_answer=False):
        """
        This method initializes an McqAnswer object.
        :param answer_key: answer key.
        :param answer: answer to the question.
        :param is_true_answer: If the answer is correct, the value is True, otherwise False.
        """
        self.answer_key = answer_key
        self.answer: str = answer
        self.is_true_answer: bool = is_true_answer


class MultipleChoiceQuestion(Component, ShuffleableQuestion):
    """
    This class represents one question on the test.
    """

    def __init__(self, question: str, answers: list[str], true_answer: str,
                 solution: str = "", num_column: int = 1, auto_end_mark=True):
        self.question: str = question
        """Content of the question."""
        self.answers: list[MultipleChoiceAnswer] = self.__get_answer_list(answers, true_answer)
        """Question answers"""
        self.num_column = num_column
        """Number of columns for which the answer will be presented."""
        self.solution = solution
        """Solution of the question"""
        self.auto_end_mark = auto_end_mark

    @staticmethod
    def __get_answer_list(answers: list[str], true_answer: str) -> list[MultipleChoiceAnswer]:
        """
        Generate a list of answer object from answer and true answer key
        :param answers: question answer list.
        :param true_answer: answer key of true answer.
        :return: a list of answer object.
        """
        answer_key = get_answer_key()
        answer_list_size = min(len(answer_key), len(answers))
        answer_list: list[MultipleChoiceAnswer] = []
        for i in range(0, answer_list_size):
            answer_list.append(MultipleChoiceAnswer(answer_key[i], answers[i], answer_key[i] in [*true_answer]))
        return answer_list

    def shuffle_content(self, seed: int = None):
        """Shuffle answer list of the question"""
        if seed is not None:
            random.seed(seed)

        num_answer = len(self.answers)
        answer_key = get_answer_key()[0:num_answer]
        random.shuffle(answer_key)
        for i in range(num_answer):
            self.answers[i].answer_key = answer_key[i]
        self.answers = sorted(self.answers, key=lambda x: x.answer_key)

    def get_true_answer_key(self) -> str:
        """Get all answer key of true answer"""
        true_answer = ""
        for answer in self.answers:
            if answer.is_true_answer:
                true_answer += answer.answer_key
        return true_answer

    def generate_exam(self) -> str:
        column_size = 1 / self.num_column
        answer_string = ""
        for i, answer in enumerate(self.answers):
            seperator = "\\\\\n" if ((i + 1) % self.num_column == 0) else "&"
            ending_punctuation = "." if self.auto_end_mark and \
                (answer.answer[-1] not in [".", "!", "?"]) else ""
            answer_string += (fr"\textbf{{{answer.answer_key}}}. " +
                fr"{answer.answer}{ending_punctuation} {seperator} ")

        return jinja_env.get_template("exam/mcq.tex").render(
            question=self.question,
            num_column=self.num_column,
            column_size=column_size,
            answer_string=answer_string
        )

    def generate_answer(self) -> str:
        return jinja_env.get_template("answer/mcq.tex").render(
            true_answer=self.get_true_answer_key()
        )

    def generate_solution(self) -> str:
        return jinja_env.get_template("solution/mcq.tex").render(
            question=self.generate_exam(),
            solution=self.solution
        )
