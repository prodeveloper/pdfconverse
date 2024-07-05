from pypdf import PdfReader
import google.generativeai as genai
import dbm
from .page import PDFConversePage
from .models import GeminiSetup,FilePath

class PDFConverse:
    """
    A class to interact with PDF files using Google's generative AI and a persistent cache.

    Attributes:
        pdf_path (str): The file path to the PDF document.
        gemini_setup (GeminiSetup): The setup for the generative AI service.
    """
    def __init__(self,gemini_setup:GeminiSetup,file_path:FilePath=None,bytes:bytes=None):
        if file_path is None and bytes is None:
            raise ValueError("Either file_path or bytes must be provided")
        self.pdf_path = file_path if file_path is not None else bytes
        self.gemini_setup = gemini_setup
        self.bytes = bytes

    
    def setup_genai(self):
        genai.configure(api_key=self.gemini_setup.api_key)
        self.model= genai.GenerativeModel(self.gemini_setup.model)
    def page(self, page_start: int, page_end: int):
        self.page_start = page_start
        self.page_end = page_end
        self.setup_genai()
        if isinstance(self.pdf_path,FilePath):
            return PDFConversePage(pdf_path=self.pdf_path.path, page_start=self.page_start, page_end=self.page_end,model=self.model)
        else:
            return PDFConversePage(pdf_path=self.bytes, page_start=self.page_start, page_end=self.page_end,model=self.model)
    def PDF(self):
        return PdfReader(pdf_path=self.pdf_path.path)