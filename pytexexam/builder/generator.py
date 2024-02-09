import os
from enum import Enum

from pytexexam.component.component import Component
from pytexexam.jinja2env import jinja_env


class ExamFileType(Enum):
    """Class present all export exam options: PDF and TEX"""
    PDF = 0
    TEX = 1


class ExamPaperType(Enum):
    """Class present all export exam options: PDF and TEX"""
    EXAM_PAPER = 0
    ANSWER_PAPER = 1
    SOLUTION_PAPER = 2


class ExamGenerator:
    """Builder class to create exam,answer and solution paper"""
    def __init__(self):
        self.__preamble = []
        self.__components = []
        self.__question_word = "Question"
        self.__answer_word = "Answer"
        self.__solution_word = "Solution"

    def generate_exam(self, file_dir: str, export_type: ExamFileType, generate_answer=True, generate_solution=True):
        if export_type == ExamFileType.TEX:
            self.export_tex_file(ExamPaperType.EXAM_PAPER, file_dir)
            if generate_answer:
                self.export_tex_file(ExamPaperType.ANSWER_PAPER, file_dir)
            if generate_solution:
                self.export_tex_file(ExamPaperType.SOLUTION_PAPER, file_dir)
        else:
            self.export_pdf_file(ExamPaperType.EXAM_PAPER, file_dir)
            if generate_answer:
                self.export_pdf_file(ExamPaperType.ANSWER_PAPER, file_dir)
            if generate_solution:
                self.export_pdf_file(ExamPaperType.SOLUTION_PAPER, file_dir)

    def add_component(self, component: Component):
        self.__components.append(component)

    def add_preamble_array(self, preamble_array: list[str]):
        self.__preamble.extend(preamble_array)

    def get_latex_string(self, paper_type: ExamPaperType) -> str:
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

        return jinja_env.get_template("generator/exam.tex").render(
            question_theorem=self.__question_word,
            answer_theorem=self.__answer_word,
            solution_theorem=self.__solution_word,
            user_preamble=self.generate_preamble(),
            component_code=component_code
        )

    def generate_preamble(self):
        return "\n".join(self.__preamble)

    def export_tex_file(self, paper_type: ExamPaperType, file_dir: str):
        """Export to .tex file"""
        if paper_type == ExamPaperType.EXAM_PAPER:
            file = open(f"{file_dir}_exam.tex", "w")
        elif paper_type == ExamPaperType.ANSWER_PAPER:
            file = open(f"{file_dir}_answer.tex", "w")
        else:
            file = open(f"{file_dir}_solution.tex", "w")
        file.write(self.get_latex_string(paper_type))
        file.close()

    def export_pdf_file(self, paper_type: ExamPaperType, file_dir: str):
        """Export to pdf file"""
        self.export_tex_file(paper_type, file_dir)
        if paper_type == ExamPaperType.EXAM_PAPER:
            os.system(f"pdflatex {file_dir}_exam.tex")
        elif paper_type == ExamPaperType.ANSWER_PAPER:
            os.system(f"pdflatex {file_dir}_answer.tex")
        else:
            os.system(f"pdflatex {file_dir}_solution.tex")
