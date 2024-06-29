from pdfconverse.pdfconverse import PDFConverse
from pdfconverse.mock_model import MockModel
from pdfconverse.models import GeminiSetup,FilePath
import os
from dotenv import load_dotenv

load_dotenv()

def test_main_flow():

    pdf_path = "./src/pdfconverse/samples/gemini_test_file.pdf"
    gemini_key = os.getenv("GEMINI_TEST_KEY")
    gemini_setup=GeminiSetup(api_key=gemini_key,model="gemini-1.5-flash")
    pdf_path=FilePath(path=pdf_path)
    pdfconverse = PDFConverse(pdf_path=pdf_path, gemini_setup=gemini_setup)
    text = pdfconverse.page(page_start=0, page_end=0).prompt("This is a test prompt:")
    assert("Yes I am live" in text)