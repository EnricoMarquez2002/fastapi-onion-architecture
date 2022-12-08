from pydantic import BaseModel


class OrdersSchema(BaseModel):
    preco_pedido: float

    class Config:
        orm_mode=True