from exam import Exam
from question import Question


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

    def __print_question(self, question: Question) -> str:
        return """
        \\begin{{question}}
        {question_content}

        \\begin{{tabular}}{ m{{0.5\\linewidth}} m{{0.5\\linewidth}} }
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
        """.format(question_content=question.question, answer_1=question.answer_list[0],
                   answer_2=question.answer_list[1], answer_3=question.answer_list[2],
                   answer_4=question.answer_list[3])

    def export_tex_file(self, file_name: str):
        # TODO: export tex.
        pass

    def export_pdf_file(self, file_name: str):
        # TODO: export pdf.
        pass
