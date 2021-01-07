from latexpaper import LatexPaper


class LatexExamPaper(LatexPaper):
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions = list()
        self.footer = ""

    def __print_question(self):
        pass

    def get_latex_string(self) -> str:
        pass


class LatexExamAnswer(LatexPaper):
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions = list()
        self.footer = ""

    def __print_answer(self):
        pass

    def get_latex_string(self) -> str:
        pass


class LatexExamSolution(LatexPaper):
    def __init__(self):
        self.preamble = ""
        self.header = ""
        self.questions = list()
        self.footer = ""

    def __print_solution(self):
        pass

    def get_latex_string(self) -> str:
        pass
