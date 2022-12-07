from sqlalchemy import Column, String, Boolean, Float
from base_app.entities.base import BaseModel

class Products(BaseModel):

    __tablename__ = 'produto_produto'

    id_produto = Column(String(100), primary_key=True) 
    nome = Column(String(100))
    preco = Column(Float(8,2))
    preco_atual = Column(Float(8,2)) 
    promocao = Column(Boolean, default=False)

    #order_product = relationship("ProductsOrder", back_populates="product_owner")