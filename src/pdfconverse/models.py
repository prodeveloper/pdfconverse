from pydantic import BaseModel, validator
from pathlib import Path

class FilePath(BaseModel):
    path: str

    @validator('path')
    def validate_path(cls, v):
        if not Path(v).is_file():
            raise ValueError(f'The path {v} is not a valid file')
        return v

class GeminiSetup(BaseModel):
    api_key: str
    model: str

class PDFText(BaseModel):
    text: str