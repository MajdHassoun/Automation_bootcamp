from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'
    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    grade = Column(Float)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student_a = Students(id=112, name="Tzahi", grade="20")
student_b = Students(id=102123, name="Majd", grade="100")

session.add_all([student_a, student_b])
session.commit()

students = session.query(Students).all()

for student in students:
    print(f"{student.name}'s grade is {student.grade} and his id is {student.id}")

session.close()

# CREATE TABLE Products(
#  ProductID INT PRIMARY KEY,
#  Name VARCHAR(50),
#  Price VARCHAR(50)
# );
#
# CREATE TABLE OrderDetails (
#  OrderDetailID INT PRIMARY KEY,
#  OrderID INT,
#  ProductID INT,
#  Quantity INT,
#  FOREIGN KEY (ProductID) REFERENCES Customers(ProductID),
# FOREIGN KEY (OrderID) REFERENCES Customers(OrderID)
# );
