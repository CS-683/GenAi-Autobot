from abc import ABC, abstractmethod

class LLMAbs(ABC):
    @abstractmethod
    def generate_content(self, prompt):
        pass

    @abstractmethod
    def initialize(self, *args, **kwargs):
        pass

