from distlib import database
from fastapi import FastAPI

from app.routes import users, products, orders

app = FastAPI(title="E-Commerce API", version="0.1.1")

# Include routers from the routes folder
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])


# Define startup and shutdown events
@app.on_event("startup")
async def startup():
    # connect to database. intitalize the cache
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    # clean up resources
    ...


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)