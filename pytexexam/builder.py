from enum import Enum
from typing import List

from latexexam import LatexExamPaper, LatexExamAnswer, LatexExamSolution
from latexpaper import LatexPaper
from question import Question
import random


class LatexExamBuilder:
    """Builder class to create exam,answer and solution paper"""
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions: List[Question] = list()
        self.footer = ""
        self.export_type: ExamExportType = ExamExportType.TEX

    def create_exam(self, file_dir: str):
        """Create exam paper"""
        exam = LatexExamPaper()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def create_answer(self, file_dir: str):
        """Create answer key paper"""
        exam = LatexExamAnswer()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def create_solution(self, file_dir: str):
        """Create solution paper"""
        exam = LatexExamSolution()
        exam.preamble = self.preamble
        exam.header = self.header
        exam.questions = self.questions
        exam.footer = self.footer
        self.__export(exam, file_dir)

    def __export(self, paper: LatexPaper, file_dir: str):
        """Export exam to .tex file or pdf file"""
        if self.export_type == ExamExportType.TEX:
            paper.export_tex_file(file_dir)
        elif self.export_type == ExamExportType.PDF:
            paper.export_pdf_file(file_dir)
        else:
            paper.export_tex_file(file_dir)

    def add_question(self, question: str, answer: List[str], true_answer: str, answer_column: int, solution: str = ""):
        """
        Add question to exam

        :param question: question stem
        :param answer: List of answers in order A, B, C, D
        :param true_answer: Answer key of true answer.
        :param answer_column: Number of columns used to present the answer
        :param solution: Solution for this question
        """
        question = Question(question, answer, true_answer, solution, answer_column)
        self.questions.append(question)

    def shuffle_all_question(self, seed: int = None):
        """
        Shuffle all question in exam

        :param seed: random seed
        """
        if seed is not None:
            random.seed(seed)
        random.shuffle(self.questions)

    def shuffle_question(self, start_index: int, end_index: int, seed: int = None):
        """
        shuffle question from start_index to end_index
        """
        if seed is not None:
            random.seed(seed)

        copy = self.questions[start_index:end_index]
        random.shuffle(copy)
        self.questions[start_index:end_index] = copy

    def shuffle_answer(self, not_shuffle=None, seed: int = None):
        """
        Shuffle question answer

        :param not_shuffle: Index list of questions that do not shuffle answers
        :param seed: random seed
        """
        if not_shuffle is None:
            not_shuffle = []

        if seed is not None:
            random.seed(seed)

        for index, question in enumerate(self.questions):
            if index not in not_shuffle:
                question.shuffle_answer()


class ExamExportType(Enum):
    """Class present all export exam options: PDF and TEX"""
    PDF = 0
    TEX = 1
