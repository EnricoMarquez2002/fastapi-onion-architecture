from fastapi import APIRouter
from .use_cases import GetUserById, CreateUser, UpdateUser, GetAllUsers
from .models.post_user import UserSchemaCreate
from .models.update_user import UserSchemaUp


router = APIRouter(
    prefix='/user',
    tags=["Users"]
)


@router.get('/{id}')
async def read_user(user_id: str):
    user = GetUserById.execute(user_id)
    return user

@router.get('')
async def read_all_users():
    users = GetAllUsers.execute()
    return users

@router.post('')
async def create_user(user_schema:UserSchemaCreate):
    user = CreateUser.execute(user_schema)
    return user

@router.patch('')
async def update_user(user_id: str, user: UserSchemaUp):
    user_up = UpdateUser.execute(user_id, user)
    return user_up