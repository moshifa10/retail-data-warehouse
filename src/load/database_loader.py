from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

from src.database.base import Base

# Register Models
from src.models.product import Product
from src.models.customer import Customer
from src.models.store import Store
from src.models.sale import Sale

from src.models.product import Product

engine = create_engine("sqlite:///database/retail_warehouse.db")

SessionLocal = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(engine)
