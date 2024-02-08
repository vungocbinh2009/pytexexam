from abc import ABC, abstractmethod
from typing import Protocol


class Component(ABC):
    """Abstract class for all component in pytexexam package"""
    @abstractmethod
    def generate_exam(self) -> str:
        """Generate latex to use in exam paper"""
        pass

    @abstractmethod
    def generate_answer(self) -> str:
        """Generate latex to use in answer paper"""
        pass

    @abstractmethod
    def generate_solution(self) -> str:
        """Generate latex to use in solution paper"""
        pass


class ShuffleableQuestion(Protocol):
    def shuffle_content(self, seed: int = None):
        pass
