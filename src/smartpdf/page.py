from pypdf import PdfReader
import dbm
from pypdf import PdfReader
from .interfaces.model import Model
from .validators import PreFlightValidator

class SmartPDFPage:

    def __init__(self,*,pdf_path:str, page_start: int, page_end: int, model:Model):
        self.page_start = page_start
        self.page_end = page_end
        self.pdf_path = pdf_path
        PreFlightValidator.page_out_of_bounds(pdf_path=pdf_path, page_start=page_start, page_end=page_end)
        self.model = model
        self.text = None
        self.extract_text()

    def extract_text(self):
        if self.text is None:
            self.text = ''
            reader = PdfReader(self.pdf_path)
            for i in range(self.page_start,self.page_end+1):
                page = reader.pages[i]
                self.text += page.extract_text()
        return self.text


    def prompt(self,prompt: str):
        prompt = prompt + ":" + self.text
        response = self.model.generate_content(prompt)
        return response.text
    
    


    
    