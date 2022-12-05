from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from ...base_app.entities.base import BaseModel
from ...users.entities.users import Users
from ...products.entities.products import Products


class Orders(BaseModel):
    __tablename__ = 'orders'

    number_of_order = Column(String(100), primary_key=True)
    order_status = Column(Integer)
    price = Column(Float(8,2))
    fk_user_id = Column(String(100), ForeignKey("users.id", ondelete='CASCADE'), nullable=True)  

    owner = relationship("Users", back_populates="order_order", lazy="joined")
    product_order = relationship("ProductsOrder", back_populates="order_owner")


