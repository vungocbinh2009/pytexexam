# pytexexam

A simple library for writing and printing exam in Python.

[![Downloads](https://pepy.tech/badge/pytexexam)](https://pepy.tech/project/pytexexam)
[![Downloads](https://pepy.tech/badge/pytexexam/month)](https://pepy.tech/project/pytexexam)
[![Downloads](https://pepy.tech/badge/pytexexam/week)](https://pepy.tech/project/pytexexam)
[![Run on Repl.it](https://repl.it/badge/github/vungocbinh2009/pytexexam)](https://repl.it/github/vungocbinh2009/pytexexam)

## About this branch
- This branch includes the source code of the upcoming pytexexam version (3.0)
- Objective: Redesign package to generalize exam generation process and include more question types instead of MCQ only in pytexexam 2.x
The project is not complete yet.

Install from github, using pip (for testing only)
```shell
pip install git+https://github.com/vungocbinh2009/pytexexam.git@pytexexam_3.x#egg=pytexexam
```

## How to use
```python
from pytexexam.component import Text, MultipartQuestion, OpenQuestion, ComponentGroup, MultipleChoiceQuestion, QuestionPart
from pytexexam.latex_util import two_column_header
from pytexexam import ExamGenerator, ExamFileType


# Create an exam generator object
exam = ExamGenerator()

# Then, you can create "component" to add to your exam.

# Create a text component to use as header.
header = Text(two_column_header("Left column", "Right column"))

# Create a multiple choice question and shuffle answer.
q1 = MultipleChoiceQuestion(
    question="This is a multiple choice question",
    answers=["Answer 1", "Answer 2", "Answer 3", "Answer 4"],
    true_answer="AB",
    num_column=4,
    solution="Multiple choice question solution"
)
q1.shuffle_content()

# Create a question with multi part whose can shuffle it part
q2 = MultipartQuestion(
    question_stem="Answer all the question below",
    prompts=[
        QuestionPart("Question part 1", "Answer 1", "Solution 1"),
        QuestionPart("Question part 2", "Answer 2", "Solution 2"),
        QuestionPart("Question part 3", "Answer 3", "Solution 3"),
        QuestionPart("Question part 4", "Answer 4", "Solution 4"),
    ],
    num_column=2
)
q2.shuffle_content()

# Create a open question
q3 = OpenQuestion(
    question="This is an open question",
    answer="This is open question answer",
    solution="This is open question answer"
)

# Create text to split each part of the test.
text = Text(r"\section{{An exam section}}")

# You can subclass "Component" from pytexexam.component
# to create your own question type.

# Create a question group to add all component together, add to exam generator
q_group = ComponentGroup([header, q1, text, q2, q3])
exam.add_component(q_group)

# Add preamble.
exam.add_preamble_array([
    r"\usepackage[utf8]{vietnam}"
])

# Generate exam
exam.generate_exam("exam1", ExamFileType.PDF)
```

## Contribution.
Contribution are welcome. Create a pull request.
## Buy me a coffee.
If you find this project useful, you can buy me coffee through Buy me a coffee

<a href="https://www.buymeacoffee.com/vungocbinh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
## License
Apache License, Version 2.0
