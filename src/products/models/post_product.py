from pydantic import BaseModel

class ProductSchema(BaseModel):
    nome: str
    preco: int
    preco_atual: int
    promocao: bool

    class Config:
        schema_extra = {
            "example": {
                "nome": "Playstation 5",
                "preco": 4500,
                "preco_atual": 4500,
                "promocao": False
            }
        }