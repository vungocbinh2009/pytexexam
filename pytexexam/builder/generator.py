from enum import Enum

from pytexexam.paper.latexpaper import ExamPaperType
from pytexexam.component.component import Component
from pytexexam.paper.latexpaper import LatexPaper


class ExamFileType(Enum):
    """Class present all export exam options: PDF and TEX"""
    PDF = 0
    TEX = 1


class ExamGenerator:
    """Builder class to create exam,answer and solution paper"""
    def __init__(self):
        self.__preamble = []
        self.__components = []
        self.__question_word = "Question"

    def generate_exam(self, file_dir: str, export_type: ExamFileType, generate_answer=True, generate_solution=True):
        paper = LatexPaper(self.__components, self.__preamble, self.__question_word)
        if export_type == ExamFileType.TEX:
            paper.export_tex_file(ExamPaperType.EXAM_PAPER, file_dir)
            if generate_answer:
                paper.export_tex_file(ExamPaperType.ANSWER_PAPER, file_dir)
            if generate_solution:
                paper.export_tex_file(ExamPaperType.SOLUTION_PAPER, file_dir)
        else:
            paper.export_pdf_file(ExamPaperType.EXAM_PAPER, file_dir)
            if generate_answer:
                paper.export_pdf_file(ExamPaperType.ANSWER_PAPER, file_dir)
            if generate_solution:
                paper.export_pdf_file(ExamPaperType.SOLUTION_PAPER, file_dir)

    def add_component(self, component: Component):
        self.__components.append(component)

    def add_preamble_array(self, preamble_array: list[str]):
        self.__preamble.extend(preamble_array)
