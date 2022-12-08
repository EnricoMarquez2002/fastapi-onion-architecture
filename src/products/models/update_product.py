from pydantic import BaseModel
from .post_product import ProductSchema
from typing import Optional


class ProductSchemaUp(ProductSchema):
    nome: Optional[str]
    preco: Optional[int]
    preco_atual: Optional[int]
    promocao: Optional[bool]