from pytexexam.component.component import Component


class Text(Component):
    """Class present a chuck of latex code"""
    def __init__(self, text: str):
        self.text = text

    def generate_exam(self):
        """Generate latex to use in exam paper"""
        return self.text + "\n\n"

    def generate_answer(self):
        """Generate latex to use in answer paper"""
        return self.text + "\n\n"

    def generate_solution(self):
        """Generate latex to use in solution paper"""
        return self.text + "\n\n"
