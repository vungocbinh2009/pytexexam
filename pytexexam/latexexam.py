from exam import Exam
from question import Question
import os


class LatexExam:
    def __init__(self, exam_title: str, exam: Exam):
        self.exam_content: Exam = exam
        self.latex_preamble: str = """
        \\documentclass[12pt,a4paper,notitlepage]{article}
        \\usepackage[utf8]{vietnam}
        \\usepackage{amsmath}
        \\usepackage{amsfonts}
        \\usepackage{amssymb}
        \\usepackage{graphicx}
        \\usepackage{array}
        \\linespread{1.5}
        \\newtheorem{question}{Câu hỏi}
        """
        self.exam_title: str = exam_title

    def add_preamble(self, preamble: str):
        self.latex_preamble += ("\n" + preamble)

    @staticmethod
    def __print_question(question: Question) -> str:
        return """
        \\begin{{question}}
        {question_content}

        \\begin{{tabular}}{{ m{{0.5\\linewidth}} m{{0.5\\linewidth}} }}
        A. {answer_1}
        &
        B. {answer_2}
        \\\\
        C. {answer_3}
        &
        D. {answer_4}
        \\\\
        \\end{{tabular}}
        \\end{{question}}
        """.format(question_content=question.question, answer_1=question.get_answer(1),
                   answer_2=question.get_answer(2), answer_3=question.get_answer(3),
                   answer_4=question.get_answer(4))

    def export_tex_file(self, file_name: str):
        question_list_string = ""
        for question in self.exam_content.question_list:
            question_list_string += (self.__print_question(question) + "\n")
        latex_string = """
        {latex_preamble}
        \\begin{{document}}
        \\textbf{{
        \\begin{{center}}
        {{\\LARGE {exam_title} }}
        \\end{{center}}
        }}
        {question_list}
        \\end{{document}}
        """.format(latex_preamble=self.latex_preamble, question_list=question_list_string,
                   exam_title=self.exam_title)
        file = open(file_name, "wt")
        file.write(latex_string)

    def export_pdf_file(self, file_name: str):
        self.export_tex_file(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))
