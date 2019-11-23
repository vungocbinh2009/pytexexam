from pytexexam.answer import Answer
from pytexexam.question import Question
from pytexexam.exam import Exam
from pytexexam.latexexam import LatexExam
if __name__ == '__main__':
    question = Question("Question 1 ?")
    question.answer_1 = Answer("Answer 1", True)
    question.answer_2 = Answer("Answer 2")
    question.answer_3 = Answer("Answer 3")
    question.answer_4 = Answer("Answer 4")
    exam = Exam([question])
    latex_exam = LatexExam("Simple exam", exam)
    latex_exam.export_tex_file("test1.tex")
    latex_exam.export_pdf_file("test1.pdf")
