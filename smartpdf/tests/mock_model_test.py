from src.smartpdf.mock_model import MockModel
import os
from dotenv import load_dotenv


load_dotenv()
def test_mock_prompt():
    model = MockModel()
    output=model.prompt('This is part of a unit test, reply using smallest amount of token and ensure you say "Yes I am live"')
    assert 'alive and ready to serve!' in output
    print("we are here")
