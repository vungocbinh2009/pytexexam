from pytexexam.jinja2env import jinja_env
from pytexexam.component.component import Component


class OpenQuestion(Component):
    """
    This class present an open question.
    """
    def __init__(self, question: str, answer: str = "", solution: str = ""):
        # Question
        self.question = question
        # Answer
        self.answer = answer
        # Solution
        self.solution = solution

    def generate_exam(self) -> str:
        return jinja_env.get_template("exam/open_question.tex").render(
            question=self.question,
        )

    def generate_answer(self) -> str:
        return jinja_env.get_template("answer/open_question.tex").render(
            answer=self.answer,
        )

    def generate_solution(self) -> str:
        return jinja_env.get_template("solution/open_question.tex").render(
            question=self.generate_exam(),
            solution=self.solution
        )
