from pypdf import PdfReader
import google.generativeai as genai
import dbm
from .page import PDFConversePage

class PDFConverse:
    """
    A class to interact with PDF files using Google's generative AI and a persistent cache.

    Attributes:
        pdf_path (str): The file path to the PDF document.
        gemini_key (str): API key for accessing Google's generative AI services.
        gemini_model (str): The model identifier for the generative AI service.
    """
    def __init__(self,*,pdf_path,gemini_key,gemini_model='gemini-1.5-flash'):
        self.pdf_path = pdf_path
        self.gemini_key = gemini_key
        self.gemini_model = gemini_model
    
    def setup_genai(self):
        genai.configure(api_key=self.gemini_key)
        self.model= genai.GenerativeModel(self.gemini_model)
    def page(self, page_start: int, page_end: int):
        self.page_start = page_start
        self.page_end = page_end
        self.setup_genai()
        return PDFConversePage(pdf_path=self.pdf_path, page_start=self.page_start, page_end=self.page_end,model=self.model)
    def PDF(self):
        return PdfReader(pdf_path=self.pdf_path)