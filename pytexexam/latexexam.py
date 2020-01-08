from typing import List

from exam import Exam
from question import Question
from jinja2 import Environment, PackageLoader
import os


class LatexExam:
    """
    This class represents a exam, allowing users to print the exam and answer to a tex file
    or pdf (with latex pre-installed)
    """
    def __init__(self, exam_title: str, exam: Exam):
        self.__env = Environment(
            loader=PackageLoader('pytexexam', 'templates'),
            autoescape=False
        )
        """The environment variable is used to render latex files"""

        self.exam_content: Exam = exam
        """The content of the exam"""
        self.question_theorem = "Question"
        """The content of the beginning of each question will be printed"""
        self.solution_theorem = "Solution"
        """The content of the beginning of each detailed answer will be printed"""
        self.user_preamble: str = ""
        """Preamble of the latex file corresponds to the exam"""
        self.exam_title: str = exam_title
        """Exam name"""
        self.exam_header: str = self.__env.get_template("examheader.tex").render(exam_title=self.exam_title)
        """The presentation of the exam's header"""

    def add_user_preamble(self, preamble: str):
        """Added preamble of latex file"""
        self.user_preamble += preamble

    def __print_question(self, question: Question) -> str:
        """
        Print the question as a string

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
        """
        if question.get_answer_column() == 1:
            return self.__print_question_1(question)
        elif question.get_answer_column() == 2:
            return self.__print_question_2(question)
        else:
            return self.__print_question_4(question)

    def __print_question_1(self, question: Question) -> str:
        """
        Print the question as a column.

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
        """
        template = self.__env.get_template("mcq1.tex")
        return template.render(question=question.question, answer_a=question.get_answer("A"),
                               answer_b=question.get_answer("B"), answer_c=question.get_answer("C"),
                               answer_d=question.get_answer("D"))

    def __print_question_2(self, question: Question) -> str:
        """
        Print the question as 2 columns.

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
        """
        template = self.__env.get_template("mcq2.tex")
        return template.render(question=question.question, answer_a=question.get_answer("A"),
                               answer_b=question.get_answer("B"), answer_c=question.get_answer("C"),
                               answer_d=question.get_answer("D"))

    def __print_question_4(self, question: Question) -> str:
        """
        Print the question as 4 columns.

        :param question: Questions to print.
        :return: Character string representing the question content in latex.
        """
        template = self.__env.get_template("mcq4.tex")
        return template.render(question=question.question, answer_a=question.get_answer("A"),
                               answer_b=question.get_answer("B"), answer_c=question.get_answer("C"),
                               answer_d=question.get_answer("D"))

    def __get_questions_str(self) -> List[str]:
        """
        Get the latex code of all the questions in the exam

        :return: List of latex codes questions
        """
        questions_str: List[str] = []
        for question in self.exam_content.question_list:
            question_str = self.__print_question(question)
            questions_str.append(question_str)
        return questions_str

    def __get_solutions_str(self) -> List[str]:
        """
        Get the latex code of the answers found in all the exam questions

        :return: List of latex codes solution
        """
        template = self.__env.get_template("mcqsolution.tex")
        solutions_str: List[str] = []
        for question in self.exam_content.question_list:
            solution_str = template.render(question=self.__print_question(question),
                                           solution=question.get_solution())
            solutions_str.append(solution_str)
        return solutions_str

    def export_tex_exam(self, file_name: str):
        """
        This method proposed exam as a tex file.

        :param file_name: The file name will output.
        """
        template = self.__env.get_template("exam.tex")
        question_str_list = self.__get_questions_str()
        template.stream(questions_str=question_str_list, question_theorem=self.question_theorem,
                        user_preamble=self.user_preamble, exam_header=self.exam_header
                        ).dump(file_name)

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
        template = self.__env.get_template("answer.tex")
        template.stream(questions=self.exam_content.question_list, exam_header=self.exam_header).dump(file_name)

    def export_pdf_answer(self, file_name: str):
        """
        This method export the answer as a tex file.

        :param file_name: The file name will output.
        """
        self.export_tex_answer(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))

    def export_tex_solution(self, file_name: str):
        """Export a file containing detailed answers for each question in the exam"""
        template = self.__env.get_template("examsolution.tex")
        solution_str_list = self.__get_solutions_str()
        template.stream(solutions_str=solution_str_list, question_theorem=self.question_theorem,
                        solution_theorem=self.solution_theorem, user_preamble=self.user_preamble,
                        exam_header=self.exam_header
                        ).dump(file_name)

    def export_pdf_solution(self, file_name: str):
        """Export a file containing detailed answers for each question in the exam"""
        self.export_tex_solution(file_name)
        os.system("pdflatex {file_name}".format(file_name=file_name))
