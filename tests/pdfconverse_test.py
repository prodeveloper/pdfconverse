from pdfconverse.pdfconverse import PDFConverse
from pdfconverse.mock_model import MockModel
import os
from dotenv import load_dotenv

load_dotenv()

def test_main_flow():

    pdf_path = "./src/pdfconverse/samples/gemini_test_file.pdf"
    gemini_key = os.getenv("GEMINI_TEST_KEY")
    pdfconverse = PDFConverse(pdf_path=pdf_path, gemini_key=gemini_key)
    text = pdfconverse.page(page_start=0, page_end=0).prompt("This is a test prompt:")
    assert("Yes I am live" in text)