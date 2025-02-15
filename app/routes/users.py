from typing import List

from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserRead
from app.models.model import Users
from app.db.session import get_session
from app.core.security import get_password_hash
from sqlmodel import Session, select

router = APIRouter()

@router.post("/register", response_model=UserRead)
async def register_user(user: UserCreate, db: Session = Depends(get_session)):
    # Hash the password
    hashed_password = get_password_hash(user.password)

    db_user = Users(
        email=user.email,
        username=user.username,
        phone=user.phone,
        address=user.address,
        password_hash=hashed_password,  # Store hashed password
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.type  # `role` instead of `type`
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Ensure the user is saved correctly
    return db_user

@router.get("/users", response_model=List[UserRead])
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(Users)).all()
    return users
