import random
import string

from pytexexam.component.component import Component, ShuffleableQuestion
from pytexexam.jinja2env import jinja_env


class McqAnswer:
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


class McqQuestion(Component, ShuffleableQuestion):
    """
    This class represents one question on the test.
    """
    def __init__(self, question: str, answers: list[str], true_answer: str, solution: str, answer_column: int):
        self.question: str = question
        """Content of the question."""
        self.answers: list[McqAnswer] = self.__get_answer_list(answers, true_answer)
        """Question answers"""
        self.answer_column = answer_column
        """Number of columns for which the answer will be presented."""
        self.solution = solution
        """Solution of the question"""

    @staticmethod
    def __get_answer_list(answers: list[str], true_answer: str) -> list[McqAnswer]:
        """
        Generate a list of answer object from answer and true answer key
        :param answers: question answer list.
        :param true_answer: answer key of true answer.
        :return: a list of answer object.
        """
        answer_key = McqQuestion.__get_answer_key()
        answer_list_size = min(len(answer_key), len(answers))
        answer_list: list[McqAnswer] = []
        for i in range(0, answer_list_size):
            answer_list.append(McqAnswer(answer_key[i], answers[i], answer_key[i] in [*true_answer]))
        return answer_list

    @staticmethod
    def __get_answer_key() -> list[str]:
        """
        get list of alphabet character. (to use it as answer key)
        :return: Alphabet character list.
        """
        return list(string.ascii_uppercase)

    def shuffle_content(self, seed: int = None):
        """Shuffle answer list"""
        if seed is not None:
            random.seed(seed)

        num_answer = len(self.answers)
        answer_key = self.__get_answer_key()[0:num_answer]
        random.shuffle(answer_key)
        for i in range(num_answer):
            self.answers[i].answer_key = answer_key[i]
        self.answers = sorted(self.answers, key=lambda x: x.answer_key)

    def get_true_answer_key(self) -> str:
        """Get answer key of true answer"""
        true_answer = ""
        for answer in self.answers:
            if answer.is_true_answer:
                true_answer += answer.answer_key
        return true_answer

    def generate_exam(self) -> str:
        column_size = 1 / self.answer_column
        table_column = rf"*{{{self.answer_column}}}{{S{{m{{\dimexpr{column_size}\linewidth-2\tabcolsep\relax}}}}}}"

        answer_string = ""
        for i, answer in enumerate(self.answers):
            seperator = "\\\\\n" if ((i + 1) % self.answer_column == 0) else "&"
            answer_string += fr"\textbf{{{answer.answer_key}}}. {answer.answer}. {seperator} "

        return jinja_env.get_template("mcq.tex").render(
            question=self.question,
            table_column=table_column,
            answer_string=answer_string
        )

    def generate_answer(self) -> str:
        return self.get_true_answer_key()

    def generate_solution(self) -> str:
        return jinja_env.get_template("mcq_solution.tex").render(
            question=self.generate_exam(),
            solution=self.solution
        )
