from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    nome: str
    sobrenome: str
    email: EmailStr

    class Config:
        orm_mode=True