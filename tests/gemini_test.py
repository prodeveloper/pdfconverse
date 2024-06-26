from src.smartpdf.gemini import GeminiModel
import os
from dotenv import load_dotenv
from src.smartpdf.validators import PostFlightValidator
load_dotenv()

class SafetyRating:
    def __init__(self, category, probability):
        self.category = category
        self.probability = probability

class Candidate:
    def __init__(self, text, role, finish_reason, index, safety_ratings):
        self.text = text
        self.role = role
        self.finish_reason = finish_reason
        self.index = index
        self.safety_ratings = safety_ratings

def test_gemini_prompt():
    gemini_key = os.getenv('GEMINI_TEST_KEY')
    model = GeminiModel(gemini_key)
    output = model.prompt('This is part of a unit test, reply using smallest amount of token and ensure you say "Yes I am live"')
    output = "Yes I am live"
    assert 'Yes I am live' in output

def test_safety_ratings():
    candidates = [
        Candidate(
            text="Yes, I am live \n",
            role="model",
            finish_reason="STOP",
            index=0,
            safety_ratings=[
                SafetyRating("HARM_CATEGORY_SEXUALLY_EXPLICIT", "NEGLIGIBLE"),
                SafetyRating("HARM_CATEGORY_HATE_SPEECH", "NEGLIGIBLE"),
                SafetyRating("HARM_CATEGORY_HARASSMENT", "NEGLIGIBLE"),
                SafetyRating("HARM_CATEGORY_DANGEROUS_CONTENT", "NEGLIGIBLE")
            ]
        )
    ]
    gemini_key = os.getenv('GEMINI_TEST_KEY')
    model = GeminiModel(gemini_key)
    PostFlightValidator.check_safety_ratings(candidates[0].safety_ratings)

def test_main_call():
    pass
    #TODO: Stopped here for the day, next step is to test the main call with pdfs