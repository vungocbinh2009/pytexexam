from pytexexam.component.component import Component


class OpenQuestion(Component):
    def __init__(self, question: str, answer: str, solution: str):
        self.question = question
        self.answer = answer
        self.solution = solution

    def generate_exam(self) -> str:
        return self.question

    def generate_answer(self) -> str:
        return self.answer

    def generate_solution(self) -> str:
        return self.solution
