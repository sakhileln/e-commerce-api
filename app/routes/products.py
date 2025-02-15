from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.product import ProductCreate, ProductUpdate, ProductRead
from app.models.model import Product
from app.db.session import get_session
from sqlmodel import Session, select

router = APIRouter()

@router.get("/products", response_model=List[ProductRead])
async def get_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products

@router.get("/products/{product_id}", response_model=ProductRead)
async def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products", response_model=ProductCreate)
async def create_product(
    product_id: int,
    description: str,
    price: float,
    session: Session = Depends(get_session),
):
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        product.description = description
        product.price = price
        session.add(product)
        session.commit()
        return product

@router.put("/products/{product_id}", response_model=ProductUpdate)
async def update_product(
        product_id: int,
        description: str,
        price: float,
        session: Session = Depends(get_session)
):
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.description = description
    product.price = price
    session.add(product)
    session.commit()
    return product
