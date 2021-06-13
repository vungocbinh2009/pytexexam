import string
from random import SystemRandom

from answer import Answer
from jinja2env import jinja_env
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
        """Shuffle answer list"""
        SystemRandom().shuffle(self.answers)

    def get_true_answer_key(self) -> str:
        """Get answer key of true answer"""
        true_answer = ""
        for answer in self.answers:
            if answer.is_true_answer:
                true_answer += answer.answer_key
        return true_answer

    def print_question_latex(self) -> str:
        """generate latex code for this question"""
        column_size = 1 / self.answer_column
        table_column = rf"*{{{self.answer_column}}}{{S{{m{{\dimexpr{column_size}\linewidth-2\tabcolsep\relax}}}}}}"

        answer_string = ""
        for i, answer in enumerate(self.answers):
            seperator = "\\\\\n" if((i+1) % self.answer_column == 0) else "&"
            answer_string += f"\\textbf{{{answer.answer_key}}}. {answer.answer}. {seperator} "

        return jinja_env.get_template("mcq.tex").render(
            question=self.question,
            table_column=table_column,
            answer_string=answer_string
        )

    def print_solution_latex(self) -> str:
        """Generate latex code to print question and solution"""
        return jinja_env.get_template("mcqsolution.tex").render(
            question=self.print_question_latex(),
            solution=self.solution
        )
