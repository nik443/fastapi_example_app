from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import users as user_crud
from app.core.schemas.user import UserRead, UserCreate
from app.core.models import db_helper
from app.core.models.user import User



router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await user_crud.get_all_users(session)
    return users


@router.post(path="", response_model=UserRead)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user: UserCreate,
) -> User:
    user = await user_crud.create_user(session, user_create=user)
    return user
