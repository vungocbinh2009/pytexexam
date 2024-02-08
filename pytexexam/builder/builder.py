from enum import Enum

from pytexexam.component.component import Component
from pytexexam.paper.latexexam import LatexExamPaper, LatexExamAnswer, LatexExamSolution
from pytexexam.paper.latexpaper import LatexPaper


class ExamGenerator:
    """Builder class to create exam,answer and solution paper"""
    def __init__(self):
        self.__preamble = []
        self.__components = []
        self.__question_word = "Question"
        self.export_type: ExamExportType = ExamExportType.TEX

    def create_exam(self, file_dir: str):
        """Create exam paper"""
        exam = LatexExamPaper()
        exam.preamble = self.preamble
        exam.components = self.components
        self.__export(exam, file_dir)

    def create_answer(self, file_dir: str):
        """Create answer key paper"""
        exam = LatexExamAnswer()
        exam.preamble = self.preamble
        exam.components = self.components
        self.__export(exam, file_dir)

    def create_solution(self, file_dir: str):
        """Create solution paper"""
        exam = LatexExamSolution()
        exam.preamble = self.preamble
        exam.components = self.components
        self.__export(exam, file_dir)

    def __export(self, paper: LatexPaper, file_dir: str):
        """Export exam to .tex file or pdf file"""
        if self.export_type == ExamExportType.TEX:
            paper.export_tex_file(file_dir)
        elif self.export_type == ExamExportType.PDF:
            paper.export_pdf_file(file_dir)
        else:
            paper.export_tex_file(file_dir)

    def add_component(self, component: Component):
        self.__components.append(component)

    def add_preamble_array(self, preamble_array: list[str]):
        self.__preamble.extend(preamble_array)


class ExamExportType(Enum):
    """Class present all export exam options: PDF and TEX"""
    PDF = 0
    TEX = 1
