from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.product import ProductCreate, ProductUpdate, ProductRead
from app.models.model import Product
from app.db.session import get_session
from sqlmodel import Session, select

router = APIRouter()

@router.get(
    "/products",
    response_model=List[ProductRead],
    summary="Get all products",
)
async def get_products(session: Session = Depends(get_session)) -> List[ProductRead]:
    """
    Get all products
    :param session:
    :return: List of products
    """
    products = session.exec(select(Product)).all()
    return products

@router.get(
    "/products/{product_id}",
    response_model=ProductRead,
    summary="Get a single product",
)
async def get_product(product_id: int, session: Session = Depends(get_session)) -> ProductRead:
    """
    Get a single product
    :param product_id:
    :param session:
    :return: Product
    """
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post(
    "/products",
    response_model=ProductCreate,
    summary="Create a new product",
)
async def create_product(
        name: str,
        description: str,
        price: float,
        stock: int,
        category: int,
        image_url: str,
        session: Session = Depends(get_session),
) -> ProductCreate:
    """
    Create a new product
    :param name:
    :param description:
    :param price:
    :param stock:
    :param category:
    :param image_url:
    :param session:
    :return: Product
    """
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


@router.put(
    "/products/{product_id}",
    response_model=ProductUpdate,
    summary="Update a single product",
)
async def update_product(
        product_id: int,
        description: str,
        price: float,
        session: Session = Depends(get_session),
) -> ProductUpdate:
    """
    Update a single product
    :param product_id:
    :param description:
    :param price:
    :param session:
    :return: Product
    """
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.description = description
    product.price = price
    session.commit()
    session.refresh(product)
    return product
