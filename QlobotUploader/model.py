from pydantic import BaseModel

class Account(BaseModel):
    username: str
    password: str
    start: int
    end: int
    colect: int
