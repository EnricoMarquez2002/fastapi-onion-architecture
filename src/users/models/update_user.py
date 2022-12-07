from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioSchemaUp(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    sobrenome: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example":{
                "nome": "Pedro",
                "sobrenome": "Silva",
                "email": "pedrosilva@gmail.com",
                "password": "Senha@123"
            }   
        }
