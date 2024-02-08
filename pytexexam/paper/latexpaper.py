import os
from enum import Enum

from pytexexam.paper.jinja2env import jinja_env
from pytexexam.component.component import Component


class LatexPaper:
    """This base class is used to export exam in tex and pdf file"""
    def __init__(self):
        self.preamble = []
        self.question_word = "Question"
        self.components: list[Component] = []

    def get_latex_string(self) -> str:
        component_code = ""
        for comp in self.components:
            component_code += (comp.generate_exam() + "\n\n")

        return jinja_env.get_template("exam.tex").render(
            question_theorem=self.question_translation,
            user_preamble=self.preamble,
            component_code=component_code
        )

    def export_tex_file(self, file_dir: str):
        """Export to .tex file"""
        file = open(f"{file_dir}.tex", "w")
        file.write(self.get_latex_string())
        file.close()

    def export_pdf_file(self, file_dir: str):
        """Export to pdf file"""
        self.export_tex_file(file_dir)
        os.system(f"pdflatex {file_dir}.tex")


class ExamExportType(Enum):
    """Class present all export exam options: PDF and TEX"""
    EXAM_PAPER = 0
    ANSWER_PAPER = 1
    SOLUTION_PAPER = 2
