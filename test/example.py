from pytexexam.question import Question
from pytexexam.exam import Exam
from pytexexam.latexexam import LatexExam
if __name__ == '__main__':
    question = Question("Question 1 ?")
    question.answer_a("Answer 1", True)
    question.answer_b("Answer 2")
    question.answer_c("Answer 3")
    question.answer_d("Answer 4")
    question.shuffle_answer()

    question2 = Question("Question 2 ?")
    question2.answer_a("Answer 1", True)
    question2.answer_b("Answer 2")
    question2.answer_c("Answer 3")
    question2.answer_d("Answer 4")
    question2.set_answer_column(2)
    question2.shuffle_answer()

    question3 = Question("Question 3 ?")
    question3.answer_a("Answer 1", True)
    question3.answer_b("Answer 2")
    question3.answer_c("Answer 3")
    question3.answer_d("Answer 4")
    question3.set_answer_column(4)
    question3.shuffle_answer()

    exam = Exam([question, question2, question3])
    exam.shuffle_question()
    latex_exam = LatexExam("Simple exam", exam)
    latex_exam.add_ams_math_preamble()
    latex_exam.export_tex_exam("test1.tex")
    latex_exam.export_pdf_exam("test1.pdf")
    latex_exam.export_tex_answer("answer1.tex")
    latex_exam.export_pdf_answer("answer1.pdf")
