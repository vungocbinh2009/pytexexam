from exam import Exam
from question import Question
import inspect
import os


class LatexExam:
    """
    This class represents a exam, allowing users to print the exam and answer to a tex file
    or pdf (with latex pre-installed)
    """
    def __init__(self, exam_title: str, exam: Exam):
        self.exam_content: Exam = exam
        """The content of the exam"""
        self.question_theorem = "Question"
        """The content of the beginning of each question will be printed"""
        self.solution_theorem = "Solution"
        """The content of the beginning of each detailed answer will be printed"""
        self.latex_preamble: str = """
        \\documentclass[12pt,a4paper,notitlepage]{{article}}
        \\usepackage[utf8]{{vietnam}}
        \\usepackage{{graphicx}}
        \\usepackage{{array}}
        \\linespread{{1.5}}
        \\newtheorem{{question}}{{{question_theorem}}}
        """.format(question_theorem=self.question_theorem)
        """Preamble of the latex file corresponds to the exam"""
        self.exam_title: str = exam_title
        """Exam name"""
        self.exam_header: str = """
        \\textbf{{
        \\begin{{center}}
        {{\\LARGE {exam_title} }}
        \\end{{center}}
        }}
        """.format(exam_title=self.exam_title)
        """The presentation of the exam's header"""

    def add_preamble(self, preamble: str):
        """
        This method allows adding the necessary lines in the preamble of the latex file,
        eg usepackage ...

        :param preamble: The part to add to preamble.
        """
        self.latex_preamble += ("\n" + preamble)

    def add_ams_math_preamble(self):
        """
        Add math packages to latex preamble.
        """
        self.add_preamble("""
        \\usepackage{amsmath}
        \\usepackage{amsfonts}
        \\usepackage{amssymb}
        """)

    @staticmethod
    def __print_question(question: Question) -> str:
        if question.get_answer_column() == 1:
            return LatexExam.__print_question_1(question)
        elif question.get_answer_column() == 2:
            return LatexExam.__print_question_2(question)
        else:
            return LatexExam.__print_question_4(question)

    @staticmethod
    def __print_question_2(question: Question) -> str:
        """
        Print the question as 2 columns.

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
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
        Print the question as 4 columns.

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
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
        Print the question as a column.

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
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
        This method proposed exam as a tex file.

        :param file_name: The file name will output.
        """
        question_list_string = ""
        for question in self.exam_content.question_list:
            question_list_string += (self.__print_question(question) + "\n")
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
        This method export the exam as a pdf file.

        :param file_name: The file name will output.
        """
        self.export_tex_exam(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))

    def export_tex_answer(self, file_name: str):
        """
        This method export the answer as a tex file.

        :param file_name: The file name will output.
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
        This method export the answer as a tex file.

        :param file_name: The file name will output.
        """
        self.export_tex_answer(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))

    def export_tex_solution(self, file_name: str):
        """Export a file containing detailed answers for each question in the exam"""
        solution_string = ""
        for question in self.exam_content.question_list:
            solution_string += (self.__print_question(question) + "\n")
            solution_string += """
            \\begin{{solution}}
            {solution}
            \\end{{solution}}
            """.format(solution=question.get_solution())

        latex_string = inspect.cleandoc("""
        {latex_preamble}
        \\newtheorem{{solution}}{{{solution_theorem}}}
        \\begin{{document}}
        {exam_header}
        {solution_list}
        \\end{{document}}
        """.format(latex_preamble=self.latex_preamble, solution_theorem=self.solution_theorem,
                   exam_header=self.exam_header, solution_list=solution_string))
        file = open(file_name, "wt")
        file.write(latex_string)

    def export_pdf_solution(self, file_name: str):
        """Export a file containing detailed answers for each question in the exam"""
        self.export_tex_solution(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))
        pass
