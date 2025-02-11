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
    category: str = Field(foreign_key="category.id")
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
    parent_id: int = Field(foreign_key="category.parent_id")

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
    transaction_id : int = Field(foreign_key="payment.transaction_id")
    amount : float = Field(nullable=False)
    payment_date : datetime = Field(default_factory=datetime.now)

class OrderItem(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    order_id : int = Field(foreign_key="orders.id")
    product_id : int = Field(foreign_key="product.id")
    quantity: int = Field(default=1)
    price_at_order : int = Field(default=1)
    subtotal: float = Field(nullable=False)

user_1 = Users(
    email="sakhi@venus.io",
    username="sakhi",
    phone="34556631",
    address="1 Hyperloop Drive",
    password_hash="PajshdfqB@$!@bsd51",
    first_name="Sakhile",
    last_name="Ndlazi",
    role="admin"
)
user_2 = Users(
    email="jane@example.com",
    username="jn",
    phone="555678631",
    address="33 Ndlazi Drive",
    password_hash="hgd23#@fhFAblk?df",
    first_name="Jane",
    last_name="Doe",
    role="customer"
)

cart_1 = Cart(user_id=1)

cart_item_1 = CartItem(cart_id=1, product_id=1, quantity=2)
cart_item_2 = CartItem(cart_id=1, product_id=2, quantity=3)

category_1 = Category(
    name="Satellite",
    description="Satellites are the smallest and most basic Earth satellites",
    parent_id=1
)

product_1 = Product(
    name="Moon",
    description="The Earth's only natural satellite",
    price=100.0,
    stock=2,
    category=1,
    image_url="https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
)


# engine = create_engine("postgresql://sakhi:moon@localhost:5432/ecommerce")
engine = create_engine("sqlite:///ecommerce.db", echo=True)
print("Creating database...")
SQLModel.metadata.create_all(bind=engine)

with Session(engine) as session:
    session.add(user_1)
    session.add(user_2)
    session.add(cart_1)
    session.add(cart_item_1)
    session.add(cart_item_2)
    session.add(category_1)
    session.add(product_1)
    session.commit()
