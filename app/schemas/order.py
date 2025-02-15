from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class OrderBase(BaseModel):
    user_id: int
    order_date: datetime

class OrderCreate(OrderBase):
    status: str
    total: float
    shipping_address: str

class OrderUpdate(BaseModel):
    # All fields optional for partial updates.
    user_id: Optional[int] = None
    order_date: Optional[datetime] = None
    status: Optional[str] = None
    total: Optional[float] = None
    shipped: Optional[float] = None
    shipping_address: Optional[str] = None

class OrderRead(OrderBase):
    status: str

    class Config:
        orm_mode = True
