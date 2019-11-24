import typing
from question import Question
import random


class Exam:
    """
    Lớp này biểu diễn 1 bài kiểm tra.
    """
    def __init__(self, question_list: typing.List[Question]):
        self.question_list = question_list
        """Danh sách các câu hỏi trong bài kiểm tra"""

    def shuffle_question(self):
        """
        Phương thức này cho phép xáo trộn toàn bộ các câu hỏi trong bài kiểm tra.
        """
        r = random.SystemRandom()
        r.shuffle(self.question_list)
