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

## Documentation
If you want to see all the functions included in this library, you can find it [here](docs/_build/latex/pytexexam.pdf)

## Note.
If you use Pycharm, you can enable language injection to get Latex support inside Python script
1. Install TeXiFy IDEA.
2. Go to Settings -> Editor -> Language Injection and add new rule:
   - Language ID: Latex (.tex) sources files
   - Places patterns: + pyLiteralExpression()
3. Enable it!. Now you get Latex syntax hightlighting inside python string! Yayyy!
   
(You can also add other pattern, using method in this file: https://github.com/JetBrains/intellij-community/blob/master/python/src/com/jetbrains/python/patterns/PythonPatterns.java)
## Contribution.
Contribution are welcome. Create a pull request.
## Buy me a coffee.
If you find this project useful, you can buy me coffee through Flattr [![Flattr this
 git
 repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/@vungocbinh)

## License
Apache License, Version 2.0