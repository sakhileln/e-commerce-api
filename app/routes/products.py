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


@router.post("/products", response_model=ProductCreate)  # Changed from PUT to POST
async def create_product(
        name: str,
        description: str,
        price: float,
        stock: int,
        category: int,
        image_url: str,
        session: Session = Depends(get_session),
):
    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category=category,
        image_url=image_url
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@router.put("/products/{product_id}", response_model=ProductUpdate)
async def update_product(
        product_id: int,
        description: str,
        price: float,
        session: Session = Depends(get_session),
):
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.description = description
    product.price = price
    session.commit()
    session.refresh(product)
    return product
