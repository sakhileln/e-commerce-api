from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session
import psycopg2


class Users(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    username : Optional[str] = Field(default=None, nullable=True)
    phone: str = Field(nullable=False, unique=True)
    address: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    role: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Cart(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=datetime.now)

class CartItem(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: int = Field(default=1)

class Product(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str
    price: float = Field(nullable=False)
    stock: int = Field(nullable=False)
    # Change category type to int to match Category.id
    category: int = Field(foreign_key="category.id")
    image_url: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Reviews(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    user_id : int = Field(foreign_key="users.id")
    product_id : int = Field(foreign_key="product.id")
    rating : int = Field(default=1)
    comment : str = Field(nullable=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Orders(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    order_date : datetime = Field(default_factory=datetime.now)
    status : str = Field(nullable=False)
    total: float = Field(nullable=False)
    shipping_address : str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Category(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=True)
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")

class Shipping(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    order_id : int = Field(foreign_key="orders.id", unique=True)
    shipping_method : str = Field(nullable=False)
    tracking_number: str = Field(nullable=False)
    shipping_status : str = Field(nullable=False)
    estimate_delivery : str = Field(nullable=False)
    shipped_date: datetime = Field(default_factory=datetime.now)

class Payment(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    order_id : int = Field(foreign_key="orders.id")
    payment_method : str = Field(nullable=False)
    payment_status : str = Field(nullable=False)
    transaction_id : int = Field(nullable=False, unique=True)
    amount : float = Field(nullable=False)
    payment_date : datetime = Field(default_factory=datetime.now)

class OrderItem(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    order_id : int = Field(foreign_key="orders.id")
    product_id : int = Field(foreign_key="product.id")
    quantity: int = Field(default=1)
    price_at_order : int = Field(default=1)
    subtotal: float = Field(nullable=False)

DATABASE_URL = "postgresql://postgres:password@localhost:5432/ecommercedb"
engine = create_engine(DATABASE_URL, echo=True)

print("Creating database tables...")
SQLModel.metadata.create_all(bind=engine)
print("Tables created successfully!")

