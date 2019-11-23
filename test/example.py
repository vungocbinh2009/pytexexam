from pytexexam.question import Question
from pytexexam.exam import Exam
from pytexexam.latexexam import LatexExam
if __name__ == '__main__':
    question = Question("Question 1 ?")
    question.answer_1("Answer 1", True)
    question.answer_2("Answer 2")
    question.answer_3("Answer 3")
    question.answer_4("Answer 4")
    question.shuffle_answer()

    question2 = Question("Question 2 ?")
    question2.answer_1("Answer 1", True)
    question2.answer_2("Answer 2")
    question2.answer_3("Answer 3")
    question2.answer_4("Answer 4")
    question2.shuffle_answer()

    question3 = Question("Question 3 ?")
    question3.answer_1("Answer 1", True)
    question3.answer_2("Answer 2")
    question3.answer_3("Answer 3")
    question3.answer_4("Answer 4")
    question3.shuffle_answer()

    exam = Exam([question, question2, question3])
    exam.shuffle_question()
    latex_exam = LatexExam("Simple exam", exam)
    latex_exam.add_ams_math_preamble()
    latex_exam.export_tex_exam("test1.tex")
    latex_exam.export_pdf_exam("test1.pdf")
