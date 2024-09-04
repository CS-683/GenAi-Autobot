from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def generate_content(self, prompt):
        pass

    @abstractmethod
    def setup(self):
        pass

