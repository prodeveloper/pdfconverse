from pdfconverse.page import PDFConversePage
from pdfconverse.mock_model import MockModel
from pdfconverse.validators import PageOutOfBoundsError
import pytest

def test_smartpdf_extract_text_pdf():
    pdf_path = "./src/pdfconverse/samples/gemini_test_file.pdf"
    model = MockModel()
    page = PDFConversePage(pdf_path=pdf_path, page_start=0, page_end=0, model=model)
    assert("Hi Gemini, this file is part of a test page" in page.text.replace('\n', ' '))
def test_page_out_of_bounds():
    pdf_path = "./src/pdfconverse/samples/gemini_test_file.pdf"
    model = MockModel()
    with pytest.raises(PageOutOfBoundsError):
        page = PDFConversePage(pdf_path=pdf_path, page_start=0, page_end=100, model=model)
        page.text
