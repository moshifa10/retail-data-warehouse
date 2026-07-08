from sqlalchemy import Column, String, Integer, Date
from src.database.base import Base
from datetime import date
from sqlalchemy.orm import relationship


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Business Key
    product_id = Column(String, nullable=False, unique=True)

    # Raw data
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    supplier = Column(String, nullable=False)

    # Relationships
    sales = relationship("Sale", back_populates="product")