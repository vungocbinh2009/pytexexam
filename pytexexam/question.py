from answer import Answer
import random


class Question:
    """
    Lớp này biểu diễn 1 câu hỏi trong bài kiểm tra.
    """
    def __init__(self, question: str):
        self.question: str = question
        """Nội dung của câu hỏi."""
        self.__answer_a = Answer()
        """Nội dung của đáp án A"""
        self.__answer_b = Answer()
        """Nội dung của đáp án B"""
        self.__answer_c = Answer()
        """Nội dung của đáp án C"""
        self.__answer_d = Answer()
        """Nội dung của đáp án D"""
        self.__answer_column = 1
        """Số cột mà đáp án sẽ được trình bầy. Đáp án có thể được trình bày dưới dạng 1 cột, 
        2 cột hoặc 4 cột"""

    def answer_a(self, answer: str, true_answer=False):
        """
        Phương thức này dùng để nhập đáp án A cho câu hỏi.
        :param answer: Nội dung đáp án A
        :param true_answer: Nếu đây là đáp án đúng thì nhập True, nếu sai thì nhập False.
        """
        self.__answer_a.answer = answer
        self.__answer_a.is_true_answer = true_answer

    def answer_b(self, answer: str, true_answer=False):
        """
        Phương thức này dùng để nhập đáp án B cho câu hỏi.
        :param answer: Nội dung đáp án B
        :param true_answer: Nếu đây là đáp án đúng thì nhập True, nếu sai thì nhập False.
        """
        self.__answer_b.answer = answer
        self.__answer_b.is_true_answer = true_answer

    def answer_c(self, answer: str, true_answer=False):
        """
        Phương thức này dùng để nhập đáp án C cho câu hỏi.
        :param answer: Nội dung đáp án C
        :param true_answer: Nếu đây là đáp án đúng thì nhập True, nếu sai thì nhập False.
        """
        self.__answer_c.answer = answer
        self.__answer_c.is_true_answer = true_answer

    def answer_d(self, answer: str, true_answer=False):
        """
        Phương thức này dùng để nhập đáp án D cho câu hỏi.
        :param answer: Nội dung đáp án D
        :param true_answer: Nếu đây là đáp án đúng thì nhập True, nếu sai thì nhập False.
        """
        self.__answer_d.answer = answer
        self.__answer_d.is_true_answer = true_answer

    def get_answer(self, answer_number: int) -> str:
        """
        Phương thức này dùng để lấy đáp án của câu hỏi.
        :param answer_number: Số tương ứng với đáp án của câu hỏi. Cụ thể: muốn lấy đáp án A thì
        nhập 1, B thì nhập 2, C thì nhập 3, và D thì nhập 4.
        :return: Câu trả lời tương ứng với đáp án đã chọn.
        """
        answer_list = {
            1: self.__answer_a.answer,
            2: self.__answer_b.answer,
            3: self.__answer_c.answer,
            4: self.__answer_d.answer
        }
        return answer_list.get(answer_number, "Invalid")

    def shuffle_answer(self):
        """
        Phương thức cho phép tráo đổi các phương án trong câu hỏi.
        """
        answer_list = [self.__answer_a, self.__answer_b, self.__answer_c, self.__answer_d]
        r = random.SystemRandom()
        r.shuffle(answer_list)
        self.__answer_a = answer_list[0]
        self.__answer_b = answer_list[1]
        self.__answer_c = answer_list[2]
        self.__answer_d = answer_list[3]

    def set_answer_column(self, answer_column: int):
        """
        Phương thức này cho phép nhập vào số cột mà đáp án sẽ được trình bày khi in câu hỏi. Các
        giá trị có thể nhập vào là 1, 2, 4
        :param answer_column: Số cột mà đáp án sẽ được trình bày khi in.
        :return:
        """
        if answer_column in [1, 2, 4]:
            self.__answer_column = answer_column

    def get_answer_column(self) -> int:
        """
        Phương thức này trả về số cột mà đáp án sẽ được trình bày khi in câu hỏi. Hàm có thể trả
        về các giá trị là 1, 2, 4.
        :return: Số cột mà đáp án sẽ được trình bày khi in câu hỏi
        """
        return self.__answer_column

    def get_true_answer(self) -> str:
        """
        Phương thức này trả về kí tự tương ứng với đáp án đúng của câu hỏi. Các kĩ tự có thể là
        A, B, C, D.
        :return: Kí tự tương ứng với đáp án đúng của câu hỏi
        """
        if self.__answer_a.is_true_answer:
            return "A"
        elif self.__answer_b.is_true_answer:
            return "B"
        elif self.__answer_c.is_true_answer:
            return "C"
        else:
            return "D"
