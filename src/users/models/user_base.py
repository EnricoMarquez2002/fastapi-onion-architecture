from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):
    nome: str
    sobrenome: str
    email: EmailStr

    class Config:
        orm_mode=True