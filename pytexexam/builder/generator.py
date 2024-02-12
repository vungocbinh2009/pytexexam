import os
from enum import Enum
import re

from pytexexam.component.component import Component
from pytexexam.jinja2env import jinja_env


class ExamFileType(Enum):
    """Class present all export exam options: PDF and TEX"""
    PDF = 0
    TEX = 1


class ExamPaperType(Enum):
    """Class present all type of paper pytexexam export"""
    EXAM_PAPER = 0
    ANSWER_PAPER = 1
    SOLUTION_PAPER = 2


class ExamGenerator:
    """Builder class to create exam,answer and solution paper"""
    def __init__(self):
        # List of preamble used in this exam
        self.__preamble = []
        # List of components used in this exam
        self.__components = []
        # Translation of common word, used in exam template.
        self.__word_translation = dict(
            question="Question",
            answer="Answer",
            solution="Solution"
        )

    def generate_exam(self, file_dir: str, export_type=ExamFileType.PDF,
                      generate_answer=True, generate_solution=True):
        """
        Export exam

        :param file_dir: file path to export exam
        :param export_type: Export file type: PDF of TEX
        :param generate_answer: if False, answer paper will not export. Default is True
        :param generate_solution if False, solution paper will not export. Default is True
        """
        if export_type == ExamFileType.TEX:
            self.__export_tex_file(ExamPaperType.EXAM_PAPER, file_dir)
            if generate_answer:
                self.__export_tex_file(ExamPaperType.ANSWER_PAPER, file_dir)
            if generate_solution:
                self.__export_tex_file(ExamPaperType.SOLUTION_PAPER, file_dir)
        else:
            self.__export_pdf_file(ExamPaperType.EXAM_PAPER, file_dir)
            if generate_answer:
                self.__export_pdf_file(ExamPaperType.ANSWER_PAPER, file_dir)
            if generate_solution:
                self.__export_pdf_file(ExamPaperType.SOLUTION_PAPER, file_dir)

    def set_word_translation(self, question=None, answer=None, solution=None):
        """
        Set other word translation for exam

        :param question: Translate word "Question"
        :param answer: Translate word "Answer"
        :param solution: Translate word "Solution"
        """
        if question is not None:
            self.__word_translation["question"] = question
        if answer is not None:
            self.__word_translation["answer"] = answer
        if solution is not None:
            self.__word_translation["solution"] = solution

    def add_component(self, component: Component):
        """
        Add component to the exam.

        :param component: Component to add
        :return:
        """
        self.__components.append(component)

    def add_multiple_component(self, component_list: list[Component]):
        """
        Add multiple component to the exam.

        :param component_list: List of component to add
        :return:
        """
        self.__components.extend(component_list)

    def add_preamble_array(self, preamble_array: list[str]):
        """
        Add command to preamble of all three papers.

        :param preamble_array: Command to add.
        :return:
        """
        self.__preamble.extend(preamble_array)

    def get_latex_string(self, paper_type: ExamPaperType) -> str:
        """
        Get latex code of paper

        :param paper_type: Type of paper: Exam, Answer, Solution.
        :return:
        """
        component_code = ""
        if paper_type == ExamPaperType.EXAM_PAPER:
            for comp in self.__components:
                component_code += (comp.generate_exam() + "\n\n")
        elif paper_type == ExamPaperType.ANSWER_PAPER:
            for comp in self.__components:
                component_code += (comp.generate_answer() + "\n\n")
        else:  # Solution paper
            for comp in self.__components:
                component_code += (comp.generate_solution() + "\n\n")

        exam_code = jinja_env.get_template("generator/exam.tex").render(
            question_theorem=self.__word_translation["question"],
            answer_theorem=self.__word_translation["answer"],
            solution_theorem=self.__word_translation["solution"],
            user_preamble=self.__generate_preamble(),
            component_code=component_code.strip()
        )
        # Xóa bớt các dấu xuống dòng không cần thiết.
        return re.sub("\n{2,}", '\n\n', exam_code)

    def __generate_preamble(self) -> str:
        """
        Generate latex code to add to paper preamble.
        :return: preamble code.
        """
        return "\n".join(self.__preamble)

    def __export_tex_file(self, paper_type: ExamPaperType, file_dir: str):
        """Export paper to .tex file"""
        if paper_type == ExamPaperType.EXAM_PAPER:
            file = open(f"{file_dir}_exam.tex", "w")
        elif paper_type == ExamPaperType.ANSWER_PAPER:
            file = open(f"{file_dir}_answer.tex", "w")
        else:
            file = open(f"{file_dir}_solution.tex", "w")
        file.write(self.get_latex_string(paper_type))
        file.close()

    def __export_pdf_file(self, paper_type: ExamPaperType, file_dir: str):
        """Export paper to .pdf file"""
        self.__export_tex_file(paper_type, file_dir)
        if paper_type == ExamPaperType.EXAM_PAPER:
            os.system(f"pdflatex {file_dir}_exam.tex")
        elif paper_type == ExamPaperType.ANSWER_PAPER:
            os.system(f"pdflatex {file_dir}_answer.tex")
        else:
            os.system(f"pdflatex {file_dir}_solution.tex")
