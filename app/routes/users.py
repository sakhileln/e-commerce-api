from datetime import timedelta
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlmodel import Session, select

from app.schemas.user import UserCreate, UserRead, Token
from app.models.model import Users
from app.db.session import get_session
from app.core.security import get_password_hash, verify_password, create_access_token, verify_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post(
    "/register",
    response_model=UserRead,
    summary="Register a new user",
    description="Creates a new user and stores hashed password in the database.",)
async def register_user(user: UserCreate, db: Session = Depends(get_session)) -> UserRead:
    """
    Register a new user.

    - **email**: Email of the user (unique)
    - **username**: Chosen username
    - **phone**: Phone number (unique)
    - **address**: User's address
    - **password**: Plain text password (will be hashed)
    - **type**: Role of the user (e.g., admin, customer)
    """
    existing_user = db.query(Users).filter(Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

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


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_session)):
    user = db.query(Users).filter(Users.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return { "access_token": access_token,
             "token_type": "bearer"
    }

@router.get("/users/me", response_model=UserRead)
def read_users_me(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    username = verify_access_token(token)
    statement = select(Users).where(Users.username == username)
    user = session.exec(statement).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user





@router.get(
    "/users",
    response_model=List[UserRead],
    summary="List all users",
)
async def get_users(session: Session = Depends(get_session)) -> List[UserRead]:
    """
    List all users in the database.
    :param session:
    :return: List of users
    """
    users = session.exec(select(Users)).all()
    return users
