import pytexexam.latexexamutil as util
from pytexexam import LatexExamBuilder, ExamExportType


builder = LatexExamBuilder()
builder.preamble = util.ams_math_package()
builder.header = "This is a simple header"
builder.footer = "This is a simple footer"
builder.export_type = ExamExportType.PDF
builder.add_question(
    question="This is a simple question",
    answer=["Answer 1", "Answer 2", "Answer 3", "Answer 4"],
    true_answer="A",
    answer_column=4,
    solution="This is solution for this question",
)

builder.create_exam("exam1")
builder.create_answer("answer1")
builder.create_solution("solution1")
