from pydantic import BaseModel


class FilePath(BaseModel):
    path: str

class GeminiSetup(BaseModel):
    api_key: str
    model: str