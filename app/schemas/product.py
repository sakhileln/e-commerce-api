from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[int] = None

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

    class Config:
        orm_mode = True

class ProductRead(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True