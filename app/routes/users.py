from typing import List

from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserRead
from app.models.model import Users
from app.db.session import get_session
from sqlmodel import Session, select

router = APIRouter()

@router.post("/register", response_model = UserRead)
async def register(user: UserCreate, session: Session = Depends(get_session)):
    # hash password, create a new user
    new_user = Users(**user.dict())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.get("/users", response_model = List[UserRead]):
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(Users)).all()
    return users
