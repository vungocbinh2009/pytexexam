class OpenQuestion:
    def __init__(self, question: str, solution: str):
        self.question = question
        self.solution = solution

    def print_question_latex(self):
        return f"{self.question}"

    def print_solution_latex(self):
        return f"{self.question}\n{self.solution}"
