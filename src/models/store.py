from sqlalchemy import Column, String, Integer, Date
from ..load import database_loader as dl
from datetime import date
from sqlalchemy.orm import relationship

Base = dl.Base

class Store(Base):

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Business Key
    store_id = Column(String, nullable=False, unique=True)

    # Raw Data
    store_name = Column(String, nullable=False)
    province = Column(String, nullable=False)
    manager = Column(String, nullable=False)

    # RelationShip
    sales = relationship("Sale", back_populates="store")