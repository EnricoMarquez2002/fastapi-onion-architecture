from sqlalchemy import Column, String, Boolean, Float
from sqlalchemy.orm import relationship
from ...base_app.entities.base import BaseModel
from ...orders.entities.orders import Orders

class Products(BaseModel):

    __tablename__ = 'products'

    name = Column(String(100))
    price = Column(Float(8,2))
    updated_price = Column(Float(8,2)) 
    promotion = Column(Boolean, default=False)

    order_product = relationship("ProductsOrder", back_populates="product_owner")