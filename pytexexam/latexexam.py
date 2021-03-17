from typing import List

from jinja2env import jinja_env
from latexpaper import LatexPaper
from question import Question


class LatexExamPaper(LatexPaper):
    """This class is used to create an exam paper"""
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions: List[Question] = list()
        self.footer = ""
        self.question_translation = "Question"

    def get_latex_string(self) -> str:
        """Generate latex code"""
        question_str = ""
        for question in self.questions:
            question_str += (question.print_question_latex() + "\n\n")

        return jinja_env.get_template("exam.tex").render(
            question_theorem=self.question_translation,
            user_preamble=self.preamble,
            exam_header=self.header,
            question_str=question_str,
            exam_footer=self.footer
        )


class LatexExamAnswer(LatexPaper):
    """This class is used to create an answer keys"""
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions: List[Question] = list()
        self.footer = ""

    def get_latex_string(self) -> str:
        """Generate latex code"""
        return jinja_env.get_template("answer.tex").render(
            user_preamble=self.preamble,
            exam_header=self.header,
            questions=self.questions,
            exam_footer=self.footer
        )


class LatexExamSolution(LatexPaper):
    """Generate solution paper for this exam"""
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions = list()
        self.footer = ""
        self.question_translation = "Question"

    def get_latex_string(self) -> str:
        """Generate latex code"""
        solution_str = ""
        for question in self.questions:
            solution_str += (question.print_solution_latex() + "\n\n")
        return jinja_env.get_template("exam.tex").render(
            question_theorem=self.question_translation,
            user_preamble=self.preamble,
            exam_header=self.header,
            question_str=solution_str,
            exam_footer=self.footer
        )
