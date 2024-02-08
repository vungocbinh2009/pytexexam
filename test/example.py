import latex_util.latexexamutil as util
from pytexexam import LatexExamBuilder, ExamExportType


builder = LatexExamBuilder()
builder.preamble = f"""
    {util.ams_math_package()}
    {util.geometry_package(top=2, bottom=2, left=3, right=2)}
"""
builder.header = util.bold_title("Exam title")
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
