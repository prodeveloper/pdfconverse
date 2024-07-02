import os
from pypdf import PdfReader

class PreFlightValidator:
    def text_length(self,text:str)->None:
        if len(text) > 10000:
            raise TextLengthError("Text length is too long")
    def key_error(self, key: str) -> None:
        if not key or len(key) < 5 or not key.isalnum() or ' ' in key:
            raise KeyError("Key must be at least 5 characters long, all alphanumeric, and contain no spaces")
    @staticmethod
    def file_exists(file_path: str) -> None:
        if not os.path.exists(file_path):
            raise FileDoesNotExistError("File does not exist")
    @staticmethod
    def page_out_of_bounds(*,pdf_path:str,page_start: int, page_end: int) -> None:
        pdf_reader = PdfReader(pdf_path)
        num_pages = len(pdf_reader.pages)
        if page_start < 0 or page_start >= num_pages or page_end < 0 or page_end >= num_pages:
            raise PageOutOfBoundsError("Page number out of bounds")

class PostFlightValidator:
    @staticmethod
    def check_safety_ratings(safety_ratings) -> None:
        for i, rating in enumerate(safety_ratings):
            # TODO: Why does this bring a number at times?
            if isinstance(rating.probability, int):
                continue
            if rating.probability != 'NEGLIGIBLE':
                raise SafetyRatingError(f"Safety rating {i} {rating.category} is not NEGLIGIBLE")




class SmartPDFError(Exception):
    pass

class TextLengthError(SmartPDFError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class KeyError(SmartPDFError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class SafetyRatingError(SmartPDFError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class FileDoesNotExistError(SmartPDFError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PageOutOfBoundsError(SmartPDFError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class FailedToReadPDFError(SmartPDFError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
