import os
from enum import Enum

from pytexexam.jinja2env import jinja_env
from pytexexam.component.component import Component


class ExamPaperType(Enum):
    """Class present all export exam options: PDF and TEX"""
    EXAM_PAPER = 0
    ANSWER_PAPER = 1
    SOLUTION_PAPER = 2


class LatexPaper:
    """This base class is used to export exam in tex and pdf file"""
    def __init__(self, components: list[Component], preamble: list[str], question_word: str):
        self.preamble = preamble
        self.question_word = question_word
        self.components: list[Component] = components

    def get_latex_string(self, paper_type: ExamPaperType) -> str:
        component_code = ""
        if paper_type == ExamPaperType.EXAM_PAPER:
            for comp in self.components:
                component_code += (comp.generate_exam() + "\n\n")
        elif paper_type == ExamPaperType.ANSWER_PAPER:
            for comp in self.components:
                component_code += (comp.generate_answer() + "\n\n")
        else: # Solution paper
            for comp in self.components:
                component_code += (comp.generate_solution() + "\n\n")

        return jinja_env.get_template("exam.tex").render(
            question_theorem=self.question_word,
            user_preamble=self.generate_preamble(),
            component_code=component_code
        )

    def generate_preamble(self):
        return "\n".join(self.preamble)

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
