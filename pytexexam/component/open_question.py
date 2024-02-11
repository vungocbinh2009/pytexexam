from pytexexam.jinja2env import jinja_env
from pytexexam.component.component import Component


class OpenQuestion(Component):
    def __init__(self, question: str, answer: str = "", solution: str = ""):
        self.question = question
        self.answer = answer
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
