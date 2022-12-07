from .repo.query_user import UserRepository
from .models.post_user import UserSchema

class GetUserById():
    def execute(user_id: str):
        user = UserRepository.get_user(user_id)
        return user

class CreateUser():
    def execute(user_schema: UserSchema):
        user = UserRepository.insert_user(user_schema)
        return user