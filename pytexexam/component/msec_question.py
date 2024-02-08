from pytexexam.jinja2env import jinja_env
from pytexexam.component.component import Component, ShuffleableQuestion
import random


class MultiSectionQuestion(Component, ShuffleableQuestion):
    def __init__(self, question_stem: str, question_section: list[str], answer: str, solution: str):
        self.question_stem = question_stem
        self.question_section = question_section
        self.answer = answer
        self.solution = solution

    def shuffle_content(self, seed: int = None):
        if seed is not None:
            random.seed(seed)

        random.shuffle(self.question_section)

    def generate_exam(self) -> str:
        section_code = ""
        for sec in self.question_section:
            section_code += fr"\item {sec}"
            section_code += "\n"

        return jinja_env.get_template("msec_question.tex").render(
            question_stem=self.question_stem,
            question_section=section_code
        )

    def generate_answer(self) -> str:
        return self.answer

    def generate_solution(self) -> str:
        return self.solution
