from database.config import DBConnectionHandler
from users.entities import users
from ..models.post_user import UserSchema
import datetime
import uuid
from base_app.security.bcrypt import get_password_hash 
from fastapi import HTTPException, status


class UserRepository:
    """ Class to manage user repo """
    @classmethod
    def get_user(cls, user_id: str):
        with DBConnectionHandler() as db_connection:

            try:
                user = db_connection.session.query(users.Users.nome, users.Users.sobrenome,users.Users.email)\
                .filter(users.Users.id_usuario == user_id)\
                .all()
                return user

            finally:
                db_connection.session.close()

    @classmethod
    def insert_user(cls, user: UserSchema):
        with DBConnectionHandler() as db_connection:

            try:
                user_entitie = users.Users()
                user_entitie.ativo = True
                user_entitie.data_criacao = datetime.datetime.now()
                user_entitie.data_modificacao = datetime.datetime.now()
                user_entitie.id_usuario = uuid.uuid4()
                user_entitie.nome = user.nome.capitalize()
                user_entitie.sobrenome = user.sobrenome.capitalize()
                user_entitie.email = user.email

                hashed_password = get_password_hash(user.password)
                user_entitie.hashed_password = hashed_password        
         
                db_connection.session.add(user_entitie)
                db_connection.session.commit()

            finally:
                db_connection.session.close()
            
            return HTTPException(status_code=status.HTTP_201_CREATED, detail="User created")

         
            

         
