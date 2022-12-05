from sqlalchemy import Column, String, Boolean, DateTime
from database.config import Base
import uuid
from sqlalchemy.sql import func


class BaseModel(Base):
    __abstract__ = True

    id = Column(String(100), primary_key=True, default=uuid.uuid4)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_at = Column(DateTime(timezone=True), onupdate=func.now())