#from sqlalchemy import Column, Integer, String, ForeignKey, Float
#from sqlalchemy.orm import relationship
#from base_app.entities.base import BaseModel


#class ProductsOrder(BaseModel):
#    __tablename__ = 'products_order'

#    fk_order_id = Column(String, ForeignKey("orders.id", ondelete='CASCADE'))
#   fk_product_id = Column(String, ForeignKey("products.id", ondelete='CASCADE'))
#    price_product = Column(Float(8,2))
#    quantity = Column(Integer)

#    order_owner = relationship("Orders", back_populates="product_order")
#    product_owner = relationship("Products", back_populates="order_product")
