from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.order import OrderCreate, OrderUpdate, OrderRead
from app.models.model import Orders
from app.db.session import get_session
from sqlmodel import Session, select

router = APIRouter()

@router.get(
    "/orders",
    response_model=List[OrderRead],
    summary="Get all orders",
)
async def get_orders(session: Session = Depends(get_session)) -> List[OrderRead]:
    """
    Get all orders
    :param session:
    :return: list of orders
    """
    orders = session.query(Orders).all()
    return orders

@router.get(
    "/orders/{id}",
    response_model=OrderRead,
    summary="Get a single order",
)
async def get_order(id: int, session: Session = Depends(get_session)) -> OrderRead:
    """
    Get a single order
    :param id:
    :param session:
    :return: Order
    """
    order = session.query(Orders).filter(Orders.id == id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put(
    "/orders/{id}",
    response_model=OrderUpdate,
    summary="Update a single order",
)
async def update_order(
        id: int,  # Order ID is now required
        status: str,
        total: float,
        session: Session = Depends(get_session),
) -> OrderUpdate:
    """
    Update a single order
    :param id:
    :param status:
    :param total:
    :param session:
    :return: Order
    """
    order = session.query(Orders).filter(Orders.id == id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.total = total
    order.status = status
    session.commit()
    session.refresh(order)
    return order


@router.post(
    "/orders",
    response_model=OrderCreate,
    summary="Create a new order",
)
async def create_order(
        user_id: int,
        status: str,
        total: float,
        shipping_address: str,
        session: Session = Depends(get_session),
) -> OrderCreate:
    """
    Create a new order
    :param user_id:
    :param status:
    :param total:
    :param shipping_address:
    :param session:
    :return: Order
    """
    order = Orders(user_id=user_id, status=status, total=total, shipping_address=shipping_address)
    session.add(order)
    session.commit()
    session.refresh(order)
    return order
