from typing import List

from latexexam import LatexExamPaper, LatexExamAnswer, LatexExamSolution
from latexpaper import LatexPaper
from question import Question


class LatexExamBuilder:
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions: List[Question] = list()
        self.footer = ""
        self.export_type = "tex"

    def create_exam(self, file_dir: str):
        exam = LatexExamPaper()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def create_answer(self, file_dir: str):
        exam = LatexExamAnswer()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def create_solution(self, file_dir: str):
        exam = LatexExamSolution()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def __export(self, paper: LatexPaper, file_dir: str):
        if self.export_type == "tex":
            paper.export_tex_file(file_dir)
        elif self.export_type == "pdf":
            paper.export_pdf_file(file_dir)
        else:
            paper.export_tex_file(file_dir)

    def add_question(self, question: str, answer: List[str], true_answer: str, answer_column: int, solution: str = ""):
        question = Question(question, answer, true_answer, solution, answer_column)
        self.questions.append(question)
