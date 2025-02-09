from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session


class Users(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False)
    password_hash: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    role: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Cart(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    quantity: int = Field(default=1)
    created_at: datetime = Field(default_factory=datetime.now)

user_1 = Users(email="sakhi@venus.io", password_hash="PajshdfqB@$!@bsd51", first_name="Sakhile", last_name="Ndlazi", role="admin")
user_2 = Users(email="jane@example.com", password_hash="hgd23#@fhFAblk?df", first_name="Jane", last_name="Doe", role="customer")

cart_1 = Cart(user_id=1, quantity=2)

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(user_1)
    session.add(user_2)
    session.add(cart_1)
    session.commit()
