class Answer:
    """
    This class is used to store 1 answer in a exam question.
    """
    def __init__(self, answer: str = "", is_true_answer=False):
        """
        This method initializes an Answer object.

        :param answer: Answer to the question.
        :param is_true_answer: If the answer is true,the value is True, if false then False.
        """
        self.answer: str = answer
        self.is_true_answer: bool = is_true_answer
