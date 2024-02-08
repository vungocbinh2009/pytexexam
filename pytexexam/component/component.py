from abc import ABC, abstractmethod


class Component(ABC):
    """Abstract class for all component in pytexexam package"""
    @abstractmethod
    def generate_exam(self):
        """Generate latex to use in exam paper"""
        pass

    @abstractmethod
    def generate_answer(self):
        """Generate latex to use in answer paper"""
        pass

    @abstractmethod
    def generate_solution(self):
        """Generate latex to use in solution paper"""
        pass
