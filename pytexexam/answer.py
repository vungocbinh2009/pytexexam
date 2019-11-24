class Answer:
    """
    Lớp này dùng để lưu trữ 1 đáp án trong 1 câu hỏi của bài kiểm tra.
    """
    def __init__(self, answer: str = "", is_true_answer=False):
        """
        Phương thức này khởi tạo một đối tượng Answer.
        :param answer: Câu trả lời cho câu hỏi.
        :param is_true_answer: Tính đúng sai của câu trả lời. Nếu câu trả lời là đúng thì nhận
        giá trị True, nếu sai thì là False.
        """
        self.answer: str = answer
        self.is_true_answer: bool = is_true_answer
