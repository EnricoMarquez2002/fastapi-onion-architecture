from .repo.query_user import UserRepository
from .models.post_user import UserSchemaCreate
from .models.update_user import UserSchemaUp
import datetime


class GetUserById():
    def execute(user_id: str):
        user = UserRepository.get_user_by_id(user_id)
        return user

class CreateUser():
    def execute(user_schema: UserSchemaCreate):
        user = UserRepository.insert_user(user_schema)
        return user

class UpdateUser():
    def execute(user_id: str, user: UserSchemaUp):
        dicionario = {}
        user = dict(user)
        for key, value in user.items():
            if value is None:
                pass
            else:
                dicionario[key] = value
        dicionario["data_modificacao"] = datetime.datetime.now()

        user_up = UserRepository.update_user(user_id, dicionario)
        return user_up
        