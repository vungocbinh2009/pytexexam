from exam import Exam
from question import Question
import inspect
import os


class LatexExam:
    """
    Lớp này biểu diễn 1 bài kiểm tra, cho phép người dùng in bài kiểm tra và đáp án ra file tex
    hoặc pdf (với latex được cài sẵn)
    """
    def __init__(self, exam_title: str, exam: Exam):
        self.exam_content: Exam = exam
        """Nội dung của bài kiểm tra"""
        self.latex_preamble: str = """
        \\documentclass[12pt,a4paper,notitlepage]{article}
        \\usepackage[utf8]{vietnam}
        \\usepackage{graphicx}
        \\usepackage{array}
        \\linespread{1.5}
        \\newtheorem{question}{Câu hỏi}
        """
        """Preamble của file latex ứng với đề kiểm tra"""
        self.exam_title: str = exam_title
        """Tên bài kiểm tra"""
        self.exam_header: str = """
        \\textbf{{
        \\begin{{center}}
        {{\\LARGE {exam_title} }}
        \\end{{center}}
        }}
        """.format(exam_title=self.exam_title)
        """Phần trình bày header của bài kiểm tra"""

    def add_preamble(self, preamble: str):
        """
        Phương thức này cho phép thêm vào các dòng cần thiết trong phần preamble của file latex,
        ví dụ như usepackage...
        :param preamble: Phần cần thêm vào preamble.
        :return:
        """
        self.latex_preamble += ("\n" + preamble)

    def add_ams_math_preamble(self):
        """
        Thêm các gói lệnh toán vào latex preamble.
        :return:
        """
        self.add_preamble("""
        \\usepackage{amsmath}
        \\usepackage{amsfonts}
        \\usepackage{amssymb}
        """)

    @staticmethod
    def __print_question_2(question: Question) -> str:
        """
        In câu hỏi dưới dạng 2 cột.
        :param question: Câu hỏi cần in.
        :return: Chuổi kí tự biểu diễn nội dung câu hỏi dạng latex.
        """
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

    @staticmethod
    def __print_question_4(question: Question) -> str:
        """
        In câu hỏi dưới dạng 4 cột.
        :param question: Câu hỏi cần in.
        :return: Chuổi kí tự biểu diễn nội dung câu hỏi dạng latex.
        """
        return """
        \\begin{{question}}
        {question_content}

        \\begin{{tabular}}{{ m{{0.25\\linewidth}} m{{0.25\\linewidth}} m{{0.25\\linewidth}} m{{
        0.25\\linewidth}}}}
        A. {answer_1}
        &
        B. {answer_2}
        &
        C. {answer_3}
        &
        D. {answer_4}
        \\\\
        \\end{{tabular}}
        \\end{{question}}
        """.format(question_content=question.question, answer_1=question.get_answer(1),
                   answer_2=question.get_answer(2), answer_3=question.get_answer(3),
                   answer_4=question.get_answer(4))

    @staticmethod
    def __print_question_1(question: Question) -> str:
        """
        In câu hỏi dưới dạng 1 cột.
        :param question: Câu hỏi cần in.
        :return: Chuổi kí tự biểu diễn nội dung câu hỏi dạng latex.
        """
        return """
        \\begin{{question}}
        {question_content}

        \\begin{{tabular}}{{ m{{\\linewidth}}}}
        A. {answer_1}
        \\\\
        B. {answer_2}
        \\\\
        C. {answer_3}
        \\\\
        D. {answer_4}
        \\\\
        \\end{{tabular}}
        \\end{{question}}
        """.format(question_content=question.question, answer_1=question.get_answer(1),
                   answer_2=question.get_answer(2), answer_3=question.get_answer(3),
                   answer_4=question.get_answer(4))

    def export_tex_exam(self, file_name: str):
        """
        Phương thức này xuất đề thi dưới dạng file tex.
        :param file_name: Tên file sẽ xuất ra.
        """
        question_list_string = ""
        for question in self.exam_content.question_list:
            if question.get_answer_column() == 1:
                question_list_string += (self.__print_question_1(question) + "\n")
            elif question.get_answer_column() == 2:
                question_list_string += (self.__print_question_2(question) + "\n")
            else:
                question_list_string += (self.__print_question_4(question) + "\n")
        latex_string = inspect.cleandoc("""
        {latex_preamble}
        \\begin{{document}}
        {exam_header}
        {question_list}
        \\end{{document}}
        """.format(latex_preamble=self.latex_preamble, question_list=question_list_string,
                   exam_title=self.exam_title, exam_header=self.exam_header))
        file = open(file_name, "wt")
        file.write(latex_string)

    def export_pdf_exam(self, file_name: str):
        """
        Phương thức này xuất đề thi dưới dạng file pdf.
        :param file_name: Tên file sẽ xuất ra.
        """
        self.export_tex_exam(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))

    def export_tex_answer(self, file_name: str):
        """
        Phương thức này xuất đáp án dưới dạng file tex.
        :param file_name: Tên file sẽ xuất ra.
        """
        exam_answer = ""
        for index, question in enumerate(self.exam_content.question_list):
            exam_answer += inspect.cleandoc("\\textbf{{{index}}}: {answer}".format(index=index + 1,
                                            answer=question.get_true_answer()))
            exam_answer += "\n\n\t\t"

        latex_string = inspect.cleandoc("""
        \\documentclass{{article}}
        \\usepackage[utf8]{{inputenc}}
        \\usepackage{{multicol}}
        
        \\begin{{document}}
        {exam_header}
        \\begin{{multicols}}{{5}}
            {exam_answer}
        \\end{{multicols}}
        \\end{{document}}
        """.format(exam_answer=exam_answer, exam_header=self.exam_header))
        file = open(file_name, "wt")
        file.write(latex_string)

    def export_pdf_answer(self, file_name: str):
        """
        Phương thức này xuất đáp án dưới dạng file tex.
        :param file_name: Tên file sẽ xuất ra.
        """
        self.export_tex_answer(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))
