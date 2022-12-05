from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ...base_app.entities.base import BaseModel
from ...orders.entities.orders import Orders

class Users(BaseModel):
    __tablename__ = "users"

    name = Column(String(100), unique=False)
    last_name = Column(String(100), unique=False)
    email = Column(String(254), unique=True)
    hashed_password = Column(String(100),unique=False)
    token_acess = Column(String(300), nullable=True)
    refresh_token = Column(String(300), nullable=True)
    
    order_order = relationship("Orders", back_populates="owner")