from typing import List

from latexexam import LatexExamPaper, LatexExamAnswer, LatexExamSolution
from pytexexam import Question


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

        if self.export_type == "tex":
            exam.export_tex_file(file_dir)
        elif self.export_type == "pdf":
            exam.export_pdf_file(file_dir)
        else:
            exam.export_tex_file(file_dir)

    def create_answer(self, file_dir: str):
        exam = LatexExamAnswer()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        exam.export_tex_file(file_dir)

        if self.export_type == "tex":
            exam.export_tex_file(file_dir)
        elif self.export_type == "pdf":
            exam.export_pdf_file(file_dir)
        else:
            exam.export_tex_file(file_dir)

    def create_solution(self, file_dir: str):
        exam = LatexExamSolution()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        exam.export_tex_file(file_dir)

        if self.export_type == "tex":
            exam.export_tex_file(file_dir)
        elif self.export_type == "pdf":
            exam.export_pdf_file(file_dir)
        else:
            exam.export_tex_file(file_dir)
