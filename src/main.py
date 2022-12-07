from fastapi import FastAPI
from users import user_routes 
from products import products_routes


app = FastAPI(title="Onion")

app.include_router(user_routes.router)
app.include_router(products_routes.router)
