# pytexexam

A simple library for writing and printing exam in Python.

## Installation
```shell
pip install pytexexam
```

## How to use
```python
from pytexexam.question import Question
from pytexexam.exam import Exam
from pytexexam.latexexam import LatexExam
# Create the questions.
question = Question("Question 1 ?")
question.answer_a("Answer 1", True)
question.answer_b("Answer 2")
question.answer_c("Answer 3")
question.answer_d("Answer 4")
# If you want to shuffle your answer, use this method.
question.shuffle_answer()

question2 = Question("Question 2 ?")
question2.answer_a("Answer 1", True)
question2.answer_b("Answer 2")
question2.answer_c("Answer 3")
question2.answer_d("Answer 4")
# print your answers in 2 or 4 columns.
question2.set_answer_column(2)
question2.shuffle_answer()

question3 = Question("Question 3 ?")
question3.answer_a("Answer 1", True)
question3.answer_b("Answer 2")
question3.answer_c("Answer 3")
question3.answer_d("Answer 4")
question3.set_answer_column(4)
question3.shuffle_answer()

# Create Exam from prepared questions. 
exam = Exam([question, question2, question3])
# Shuffle the questions.
exam.shuffle_question()
# Create LatexExam to export the exam into a latex file.
latex_exam = LatexExam("Simple exam", exam)
# Add math to preamble, if needed.
latex_exam.add_ams_math_preamble()
# Export your test to tex or pdf format (requires latex already installed.
latex_exam.export_tex_exam("test1.tex")
latex_exam.export_pdf_exam("test1.pdf")
latex_exam.export_tex_answer("answer1.tex")
latex_exam.export_pdf_answer("answer1.pdf")
```

## All library API.
If you want to see all the functions included in this library, you can find the pytexexam.pdf file
 in the docs directory
## Contribution.
Contribution are welcome. Create a pull request.
## Buy me a coffee.
If you find this project useful, you can buy me coffee through Flattr [![Flattr this
 git
 repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/@vungocbinh)

## License
Apache License, Version 2.0