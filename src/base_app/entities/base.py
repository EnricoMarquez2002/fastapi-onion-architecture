from database.connection import Base
from sqlalchemy import Column, Boolean, DateTime

class BaseModel(Base):
    __abstract__ = True

    ativo = Column(Boolean, default=True)
    data_criacao = Column(DateTime)
    data_modificacao = Column(DateTime)