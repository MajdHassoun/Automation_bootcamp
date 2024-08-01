from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    email = Column(String)


class Product(Base):
    __tablename__ = 'Product'
    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    price = Column(INTEGER)




