from sqlalchemy import create_engine, Column, INTEGER, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Book(Base):
    __tablename__ = 'Book'
    id = Column(INTEGER, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

book_a = Book(id=1, title="hi", author="me", publication_date="07/06/2024")
book_b = Book(id=2, title="hello", author="you", publication_date="08/01/2023")
book_c = Book(id=3, title="bey", author="we", publication_date="22/11/2011")

session.add_all([book_a, book_b, book_c])
session.commit()

books = session.query(Book).all()

for book in books:
    print(f"title = {book.title}, author = {book.author}, date =  {book.publication_date}, id = {book.id}")

session.close()
