from pydantic import BaseModel

class LogInput(BaseModel):
    content: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str