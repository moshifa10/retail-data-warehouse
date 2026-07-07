from sqlalchemy import Column, String, Integer, Date
from ..load import database_loader as dl
from datetime import date

Base = dl.Base

class Sale(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

    # Raw Data
    transaction_id = Column(String, nullable=False)
    customer_name = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    store_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    bought_date = Column(Date, nullable=False)
    