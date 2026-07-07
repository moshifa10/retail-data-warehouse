from sqlalchemy import Column, Integer, String, Date
from ..load import database_loader as dl
from datetime import date


Base = dl.Base


class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    # Raw data
    customer_id = Column(String, nullable=False)
    customer_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    city = Column(String, nullable=False)
