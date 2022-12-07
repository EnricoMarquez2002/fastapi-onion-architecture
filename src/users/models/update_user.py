from pydantic import EmailStr
from typing import Optional
from .user_base import UserSchema


class UserSchemaUp(UserSchema):
    nome: Optional[str]
    email: Optional[EmailStr]
    sobrenome: Optional[str]
    hashed_password: Optional[str]


    class Config:
        schema_extra = {
            "example":{
                "nome": "Pedro",
                "sobrenome": "Silva",
                "email": "pedrosilva@gmail.com",
                "password": "Senha@123"
            }   
        }
