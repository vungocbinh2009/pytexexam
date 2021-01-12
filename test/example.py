from builder import LatexExamBuilder

builder = LatexExamBuilder()
builder.header = "This is a simple header"
builder.footer = "This is a simple footer"
builder.add_question(
    "This is a simple question",
    ["Answer 1", "Answer 2", "Answer 3", "Answer 4"],
    "A",
    4,
    "This is solution for this question",
)
builder.create_exam("exam1")
builder.create_answer("answer1")
builder.create_solution("solution1")
