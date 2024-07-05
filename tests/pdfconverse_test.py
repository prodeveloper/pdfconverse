from pdfconverse.pdfconverse import PDFConverse
from pdfconverse.mock_model import MockModel
from pdfconverse.models import GeminiSetup,FilePath
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

def test_file_path_flow():

    file_path = "./src/pdfconverse/samples/gemini_test_file.pdf"
    gemini_key = os.getenv("GEMINI_TEST_KEY")
    gemini_setup=GeminiSetup(api_key=gemini_key,model="gemini-1.5-flash")
    file_path=FilePath(path=file_path)
    pdfconverse = PDFConverse(gemini_setup=gemini_setup,file_path=file_path)
    text = pdfconverse.page(page_start=0, page_end=0).prompt("This is a test prompt:")
    assert("Yes I am live" in text)

def test_bites_flow():
    file_path = "./src/pdfconverse/samples/gemini_test_file.pdf"
    with open(file_path, "rb") as f:
        pdf_bytes = BytesIO(f.read())
    gemini_key = os.getenv("GEMINI_TEST_KEY")
    gemini_setup=GeminiSetup(api_key=gemini_key,model="gemini-1.5-flash")
    pdfconverse = PDFConverse(bytes=pdf_bytes, gemini_setup=gemini_setup)
    text = pdfconverse.page(page_start=0, page_end=0).prompt("This is a test prompt:")
    assert("Yes I am live" in text)