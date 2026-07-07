from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///database/retail_warehouse.db")
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)