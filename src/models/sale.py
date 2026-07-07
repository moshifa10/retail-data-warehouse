from sqlalchemy import Column, String, Integer, Date, ForeignKey
from ..load import database_loader as dl
from datetime import date
from sqlalchemy.orm import relationship

Base = dl.Base

class Sale(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

    # Business Key
    transaction_id = Column(String, nullable=False)

    # Foreign Keys

    customer_id = Column(
        String,
        ForeignKey("customers.customer_id", ondelete="CASCADE"),
        nullable=False
    )

    product_id = Column(
        String, 
        ForeignKey("products.product_id", ondelete="CASCADE"),
        nullable=False
    )

    store_id = Column(
        String,
        ForeignKey("stores.store_id", ondelete="CASCADE"),
        nullable=False
    )

    # Sale Information
    quantity = Column(Integer, nullable=False)
    bought_date = Column(Date, nullable=False)
    

    # Relationship
    customer = relationship("Customer", back_populates="sales")
    product = relationship("Sale", back_populates="sales")
    store = relationship("Store", back_populates="sales")