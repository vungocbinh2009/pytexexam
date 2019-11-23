from answer import Answer
import random


class Question:
    def __init__(self, question: str):
        self.question: str = question
        self.__answer_1 = Answer()
        self.__answer_2 = Answer()
        self.__answer_3 = Answer()
        self.__answer_4 = Answer()

    def answer_1(self, answer: str, true_answer=False):
        self.__answer_1.answer = answer
        self.__answer_1.is_true_answer = true_answer

    def answer_2(self, answer: str, true_answer=False):
        self.__answer_2.answer = answer
        self.__answer_2.is_true_answer = true_answer

    def answer_3(self, answer: str, true_answer=False):
        self.__answer_3.answer = answer
        self.__answer_3.is_true_answer = true_answer

    def answer_4(self, answer: str, true_answer=False):
        self.__answer_4.answer = answer
        self.__answer_4.is_true_answer = true_answer

    def get_answer(self, answer_number: int) -> str:
        answer_list = {
            1: self.__answer_1.answer,
            2: self.__answer_2.answer,
            3: self.__answer_3.answer,
            4: self.__answer_4.answer
        }
        return answer_list.get(answer_number, "Invalid")

    def shuffle_answer(self):
        answer_list = [self.__answer_1, self.__answer_2, self.__answer_3, self.__answer_4]
        r = random.SystemRandom()
        r.shuffle(answer_list)
        self.__answer_1 = answer_list[0]
        self.__answer_2 = answer_list[1]
        self.__answer_3 = answer_list[2]
        self.__answer_4 = answer_list[3]
