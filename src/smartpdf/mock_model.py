from .interfaces.model import Model

class MockModel(Model):
    def prompt(self, prompt: str) -> str:
        return 'alive and ready to serve!'
    def setup(self)->None:
        pass