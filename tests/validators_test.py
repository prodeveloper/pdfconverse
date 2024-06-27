from pdfconverse.validators import PreFlightValidator, TextLengthError, KeyError
import pytest

def test_text_length():
    validator = PreFlightValidator()
    validator.text_length("This is a test")
def test_long_text_length():
    validator = PreFlightValidator()
    with pytest.raises(TextLengthError):
        validator.text_length("This is a test"*10000)
def test_invalid_key():
    validator = PreFlightValidator()
    key = "some randon key"
    with pytest.raises(KeyError):
        validator.key_error(key)
