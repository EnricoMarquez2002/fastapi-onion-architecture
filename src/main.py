from fastapi import FastAPI
from users import user_routes 
from products import products_routes
from orders import order_routes


app = FastAPI(title="Onion")

app.include_router(user_routes.router)
app.include_router(products_routes.router)
app.include_router(order_routes.router)