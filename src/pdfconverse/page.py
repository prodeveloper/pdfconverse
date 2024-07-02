from pypdf import PdfReader
import dbm
from pypdf import PdfReader
from .interfaces.model import Model
from .validators import PreFlightValidator,FailedToReadPDFError
from .models import PDFText

class PDFConversePage:

    def __init__(self,*,pdf_path:str, page_start: int, page_end: int, model:Model):
        self.page_start = page_start
        self.page_end = page_end
        self.pdf_path = pdf_path
        PreFlightValidator.page_out_of_bounds(pdf_path=pdf_path, page_start=page_start, page_end=page_end)
        self.model = model
        self.pdf_text: PDFText = None
        self.extract_text()

    def extract_text(self):
        if self.pdf_text is None:
            text = ''
            try:
                reader = PdfReader(self.pdf_path)
                for i in range(self.page_start,self.page_end+1):
                    page = reader.pages[i]
                    text += page.extract_text()
            except Exception as e:
                raise FailedToReadPDFError(f"Failed to read PDF: {e}")
            self.pdf_text = PDFText(text=text)
        return self.pdf_text


    def prompt(self,prompt: str):
        prompt = prompt + ":" + self.pdf_text.text
        response = self.model.generate_content(prompt)
        return response.text
    
    


    
    