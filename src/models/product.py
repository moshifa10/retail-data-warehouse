from sqlalchemy import Column, String, Integer, Date
from ..load import database_loader as dl
from datetime import date

Base = dl.Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    # Raw Data
    product_id = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    supplier = Column(String, nullable=False)

    # Relationships