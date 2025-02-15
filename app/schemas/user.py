from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    username: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True