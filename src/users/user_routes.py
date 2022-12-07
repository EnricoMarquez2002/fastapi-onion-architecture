from fastapi import APIRouter
from .use_cases import GetUserById, CreateUser
from .models.post_user import UserSchema

router = APIRouter(
    prefix='/user',
    tags=["Users"]
)


@router.get('')
async def get_user(id: str):
    user = GetUserById.execute(id)
    return user

@router.post('')
async def create_user(user_schema:UserSchema):
    user = CreateUser.execute(user_schema)
    print(user_schema)
    return user