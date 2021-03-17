from enum import Enum
from typing import List

from latexexam import LatexExamPaper, LatexExamAnswer, LatexExamSolution
from latexpaper import LatexPaper
from question import Question


class LatexExamBuilder:
    """Builder class to create exam,answer and solution paper"""
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions: List[Question] = list()
        self.footer = ""
        self.export_type: ExamExportType = ExamExportType.TEX

    def create_exam(self, file_dir: str):
        """Create exam paper"""
        exam = LatexExamPaper()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def create_answer(self, file_dir: str):
        """Create answer key paper"""
        exam = LatexExamAnswer()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def create_solution(self, file_dir: str):
        """Create solution paper"""
        exam = LatexExamSolution()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def __export(self, paper: LatexPaper, file_dir: str):
        """Export exam to .tex file or pdf file"""
        if self.export_type == ExamExportType.TEX:
            paper.export_tex_file(file_dir)
        elif self.export_type == ExamExportType.PDF:
            paper.export_pdf_file(file_dir)
        else:
            paper.export_tex_file(file_dir)

    def add_question(self, question: str, answer: List[str], true_answer: str, answer_column: int, solution: str = ""):
        """Add question to exam"""
        question = Question(question, answer, true_answer, solution, answer_column)
        self.questions.append(question)


class ExamExportType(Enum):
    """Class present all export exam options"""
    PDF = 0
    TEX = 1
