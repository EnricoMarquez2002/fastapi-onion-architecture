from fastapi import FastAPI
from users import routes 



app = FastAPI(title="Onion")

app.include_router(routes.router)