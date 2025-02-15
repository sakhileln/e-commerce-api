from fastapi import FastAPI
from sqlmodel import SQLModel

from app.routes import users, products, orders
from app.core.config import settings
from app.db.session import engine

app = FastAPI(title="E-Commerce API", version="0.1.1")

# Ensure tables are created only once (persistent)
SQLModel.metadata.create_all(engine)

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
