from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: Optional[int] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

    class Config:
        orm_mode = True

class ProductRead(ProductBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
