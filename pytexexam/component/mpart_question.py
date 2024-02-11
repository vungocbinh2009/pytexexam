from pytexexam.latex_util.internal import get_alpha_numbering_key
from pytexexam.jinja2env import jinja_env
from pytexexam.component.component import Component, ShuffleableQuestion
import random


class QuestionPart:
    def __init__(self, prompt: str, answer: str = "", solution: str = ""):
        self.prompt = prompt
        self.answer = answer
        self.solution = solution


class MultipartQuestion(Component, ShuffleableQuestion):
    """
    This class presents question with one question stem and multiple prompt (sub-question),
    which can be shuffled
    """
    def __init__(self, question_stem: str, prompts: list[QuestionPart], num_column: int = 1):
        # Question stem
        self.question_stem = question_stem
        # List of prompts
        self.prompts = prompts
        # Number of column when present prompt list
        self.num_column = num_column

    def shuffle_content(self, seed: int = None):
        """
        Shuffle prompt list of the question
        :param seed: seed value
        :return:
        """
        if seed is not None:
            random.seed(seed)

        random.shuffle(self.prompts)

    def generate_exam(self) -> str:
        column_size = 1 / self.num_column
        question_prompts_str = ""
        prompt_numbering = get_alpha_numbering_key()
        for i, prompt in enumerate(self.prompts):
            seperator = "\\\\\n" if ((i + 1) % self.num_column == 0) else "&"
            question_prompts_str += fr"{prompt_numbering[i]}. {prompt.prompt}. {seperator} "

        return jinja_env.get_template("exam/mpart.tex").render(
            question_stem=self.question_stem,
            num_column=self.num_column,
            column_size=column_size,
            question_prompts_str=question_prompts_str
        )

    def generate_answer(self) -> str:
        answer_list = list(map(lambda x: x.answer, self.prompts))
        prompt_numbering = get_alpha_numbering_key()
        question_answer_str = ""
        for i, ans in enumerate(answer_list):
            question_answer_str += f"{prompt_numbering[i]}. {ans}\n\n"

        return jinja_env.get_template("answer/mpart.tex").render(
            answer=question_answer_str
        )

    def generate_solution(self) -> str:
        solution_list = list(map(lambda x: x.solution, self.prompts))
        prompt_numbering = get_alpha_numbering_key()
        question_solution_str = ""
        for i, sol in enumerate(solution_list):
            question_solution_str += f"{prompt_numbering[i]}. {sol}\n\n"

        return jinja_env.get_template("solution/mpart.tex").render(
            question=self.generate_exam(),
            solution=question_solution_str
        )
