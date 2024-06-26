from .interfaces.model import Model
import google.generativeai as genai
from .validators import PostFlightValidator, SafetyRatingError

class GeminiModel(Model):
    def __init__(self, gemini_key, gemini_model='gemini-1.5-flash'):
        self.gemini_key = gemini_key
        self.gemini_model = gemini_model
        self.setup()
    def setup(self) -> None:
         genai.configure(api_key=self.gemini_key)
         self.model = genai.GenerativeModel(self.gemini_model)

    def prompt(self, prompt):
        response = self.model.generate_content(prompt)
        candidates = response.candidates[0]
        PostFlightValidator.check_safety_ratings(candidates.safety_ratings)
        return response.text
