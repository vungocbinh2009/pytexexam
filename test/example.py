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
