from .user_base import UserSchema
from pydantic import validator
import re


class UserSchemaCreate(UserSchema):
    password: str

    @validator("password")
    def validate_password(cls, value: str):
        if len(value) < 8:
              raise ValueError("A senha deve conter pelo menos 8 dígitos")
        if not re.search("[A-Z]", value):
            raise ValueError("A senha de conter pelo menos uma letra maiúscula")
        if not re.search("[0-9]", value):
            raise ValueError("A senha deve conter pelo menos um número")
        if not re.search(r"[ `!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~]", value):
            raise ValueError("A senha deve conter pelo menos um carácter especial")
        return value

   

    