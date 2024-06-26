from smartpdf.page import SmartPDFPage
from smartpdf.mock_model import MockModel
from smartpdf.validators import PageOutOfBoundsError
import pytest

def test_smartpdf_extract_text_pdf():
    pdf_path = "./src/smartpdf/samples/gemini_test_file.pdf"
    model = MockModel()
    page = SmartPDFPage(pdf_path=pdf_path, page_start=0, page_end=0, model=model)
    assert("Hi Gemini, this file is part of a test page" in page.text.replace('\n', ' '))
def test_page_out_of_bounds():
    pdf_path = "./src/smartpdf/samples/gemini_test_file.pdf"
    model = MockModel()
    with pytest.raises(PageOutOfBoundsError):
        page = SmartPDFPage(pdf_path=pdf_path, page_start=0, page_end=100, model=model)
        page.text
