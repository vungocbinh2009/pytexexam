class Answer:
    """
    This class is used to store 1 answer in a question.
    """
    def __init__(self, answer_key: str, answer: str, is_true_answer=False):
        """
        This method initializes an Answer object.

        :param answer_key: Answer
        :param answer: Answer to the question.
        :param is_true_answer: If the answer is correct,the value is True, otherwise False.
        """
        self.answer_key = answer_key
        self.answer: str = answer
        self.is_true_answer: bool = is_true_answer
