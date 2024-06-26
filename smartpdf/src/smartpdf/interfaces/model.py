from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def prompt(self, prompt: str) -> str:
        pass
    @abstractmethod
    def setup(self)->None:
        pass
