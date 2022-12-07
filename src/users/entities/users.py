from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from base_app.entities.base import BaseModel
from orders.entities.orders import Orders

class Users(BaseModel):
    __tablename__ = "usuario_usuario"
    
    id_usuario = Column(String(100), primary_key=True)
    nome = Column(String(100), unique=False)
    sobrenome = Column(String(100), unique=False)
    email = Column(String(254), unique=True)
    hashed_password = Column(String(100),unique=False)
    token_acess = Column(String(300), nullable=True)
    refresh_token = Column(String(300), nullable=True)
    
    pedido_pedido = relationship("Orders", back_populates="owner")