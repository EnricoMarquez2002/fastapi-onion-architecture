from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from base_app.entities.base import BaseModel
from products.entities.products import Products


class Orders(BaseModel):
    __tablename__ = 'pedido_pedido'

    numero_pedido = Column(String(100), primary_key=True)
    status_pedido = Column(Integer)
    preco_pedido = Column(Float(8,2))
    fk_UUID_usuario = Column(String(100), ForeignKey("usuario_usuario.id_usuario", ondelete='CASCADE'), nullable=True)  

    owner = relationship("Users", back_populates="pedido_pedido", lazy="joined")
    #product_order = relationship("ProductsOrder", back_populates="order_owner")


