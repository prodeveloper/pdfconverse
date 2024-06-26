from pypdf import PdfReader
from smartpdf.validators import PreFlightValidator, FileDoesNotExistError
import pytest

def test_extract_text_pdf():
    file_path = "./src/smartpdf/samples/gemini_test_file.pdf"
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)
        assert(num_pages==1)
        page1 = pdf_reader.pages[0]
        content = page1.extract_text().replace('\n', ' ')
        assert("Hi Gemini, this file is part of a test page" in content)
def test_file_exists():
    file_path = "./src/smartpdf/samples/gemini_test_file.pdf"
    PreFlightValidator.file_exists(file_path)
def test_filed_does_not_exist():
    file_path = "no/path.pdf"
    with pytest.raises(FileDoesNotExistError):
        PreFlightValidator.file_exists(file_path)
    