# pytexexam

A simple library for writing and printing exam in Python.
[![Run on Repl.it](https://repl.it/badge/github/vungocbinh2009/pytexexam)](https://repl.it/github/vungocbinh2009/pytexexam)
## Installation
```shell
pip install pytexexam
```

## How to use
```python
import pytexexam.latexexamutil as util
from pytexexam import LatexExamBuilder, ExamExportType

# Create exam builder
builder = LatexExamBuilder()
# You can add preamble here
builder.preamble = util.ams_math_package()
# Exam header
builder.header = "This is a simple header"
# Exam footer
builder.footer = "This is a simple footer"
# You can export exam in tex file or pdf file (need Latex installed)
builder.export_type = ExamExportType.PDF
# Add question
builder.add_question(
    question="This is a simple question",
    # Answers: This package auto add A, B, C, D ... in answers
    answer=["Answer 1", "Answer 2", "Answer 3", "Answer 4"],
    # True answer key
    true_answer="A",
    # present answer in multiple column
    answer_column=4,
    # Solution of this question
    solution="This is solution for this question",
)

# Creste exam, answer and solution!
builder.create_exam("exam1")
builder.create_answer("answer1")
builder.create_solution("solution1")
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