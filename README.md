# pytexexam

A simple library for writing and printing exam in Python.
[![Run on Repl.it](https://repl.it/badge/github/vungocbinh2009/pytexexam)](https://repl.it/github/vungocbinh2009/pytexexam)
## Installation
```shell
pip install pytexexam
```

## How to use
```python
from pytexexam import Question, Exam, LatexExam, latexexamutil

# Create questions, answers and solution.
question = Question("Question 1 ?")
question.answer_a("Answer 1", True)
question.answer_b("Answer 2")
question.answer_c("Answer 3")
question.answer_d("Answer 4")
question.shuffle_answer()
question.solution("""
This is the detailed answer of the first question.
""")

# Another way to enter answer options.
question2 = Question("Question 2 ?")
question2.answers(true_answer="A", answer_dict={
    "A": "Answer 1",
    "B": "Answer 2",
    "C": "Answer 3",
    "D": "Answer 4"
})
question2.solution("""
This is the detailed answer of the second question.
""")
question2.set_answer_column(2)
question2.shuffle_answer()

# One more question.
question3 = Question("Question 3 ?")
question3.answer_a("Answer 1", True)
question3.answer_b("Answer 2")
question3.answer_c("Answer 3")
question3.answer_d("Answer 4")
question3.set_answer_column(4)
question3.shuffle_answer()

# Create a exam from existing questions.
exam = Exam([question, question2, question3])

# Shuffle the questions.
exam.shuffle_question()

# Create a LatexExam object to export a question as a tex or pdf file (with latex pre-installed)
latex_exam = LatexExam("Simple exam", exam)
# Add AMS math packages, if needed.
latex_exam.add_user_preamble(latexexamutil.ams_math_package())

# Export exam.
latex_exam.export_tex_exam("test1.tex")
latex_exam.export_pdf_exam("test1.pdf")

# Export answer keys
latex_exam.export_tex_answer("answer1.tex")
latex_exam.export_pdf_answer("answer1.pdf")

# Export solutions.
latex_exam.export_tex_solution("solution1.pdf")
latex_exam.export_pdf_solution("solution1.pdf")
```

## All package API.
If you want to see all the functions included in this library, you can find the pytexexam.pdf
 file in the docs directory
## Contribution.
Contribution are welcome. Create a pull request.
## Buy me a coffee.
If you find this project useful, you can buy me coffee through Flattr [![Flattr this
 git
 repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/@vungocbinh)

## License
Apache License, Version 2.0