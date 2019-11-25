# pytexexam

1 thư viện đơn giản để soạn và in đề thi trên Python.

## Hướng dẫn cài đặt

## Hướng dẫn sử dụng
```python
from pytexexam.question import Question
from pytexexam.exam import Exam
from pytexexam.latexexam import LatexExam
# Tạo các câu hỏi cần thiết.
question = Question("Question 1 ?")
question.answer_a("Answer 1", True)
question.answer_b("Answer 2")
question.answer_c("Answer 3")
question.answer_d("Answer 4")
# Nếu muốn xáo trộn các phương án thì dùng phương thức này.
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
# Tạo Exam từ các câu hỏi đã soạn. 
exam = Exam([question, question2, question3])
# Xáo trộn các câu hỏi.
exam.shuffle_question()
# Tạo LatexExam để xuất đề thi sang file latex.
latex_exam = LatexExam("Simple exam", exam)
# Thêm math vào preamble, nếu cần thiết.
latex_exam.add_ams_math_preamble()
# Xuất đề thi ra định dạng tex hoặc pdf (cần có latex đã được cài đặt sẵn.
latex_exam.export_tex_exam("test1.tex")
latex_exam.export_pdf_exam("test1.pdf")
latex_exam.export_tex_answer("answer1.tex")
latex_exam.export_pdf_answer("answer1.pdf")
```

## All library API.

## Contribution.

## Buy me a coffee.
