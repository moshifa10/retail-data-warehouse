from sqlalchemy import Column, String, Integer, Date
from ..load import database_loader as dl
from datetime import date

Base = dl.Base

class Store(Base):

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)

    # Raw Data
    store_id = Column(String, nullable=False)
    store_name = Column(String, nullable=False)
    province = Column(String, nullable=False)
    manager = Column(String, nullable=False)