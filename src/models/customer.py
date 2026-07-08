from sqlalchemy import Column, Integer, String, Date
from src.database.base import Base
from datetime import date
from sqlalchemy.orm import relationship


class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Business Key
    customer_id = Column(String, nullable=False, unique=True)

    # Raw data
    customer_name = Column(String, nullable=False)
    email = Column(String)
    city = Column(String, nullable=False)

    # Relationship
    sales = relationship("Sale", back_populates="customer")
