from pydantic import BaseModel


class LogInput(BaseModel):
    content: str