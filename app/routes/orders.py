from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.order import OrderCreate, OrderUpdate, OrderRead
from app.models.model import Orders
from app.db.session import get_session
from sqlmodel import Session, select

router = APIRouter()

@router.get("/orders", response_model=List[OrderRead])
async def get_orders(session: Session = Depends(get_session)):
    orders = session.query(Orders).all()
    return orders

@router.get("/orders/{id}", response_model=OrderRead)
async def get_order(id: int, session: Session = Depends(get_session)):
    order = session.query(Orders).filter(Orders.id == id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/orders/{id}", response_model=OrderUpdate)
async def update_order(
        status: str,
        total: float,
        session: Session = Depends(get_session),
):
    order = session.query(Orders).filter(Orders.status == status).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.total = total
    order.status = status
    session.commit()
    return order

@router.put("/orders", response_model=OrderCreate)
async def create_order(
        status: str,
        total: float,
        session: Session = Depends(get_session),
):
    order = Orders(status=status, total=total)
    session.add(order)
    session.commit()
    return order