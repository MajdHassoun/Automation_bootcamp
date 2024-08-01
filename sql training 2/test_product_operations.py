import unittest
from sqlalchemy import create_engine
from models import Base, Product
from sqlalchemy.orm import sessionmaker


class TestProductOperations(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.product_a = Product(name="Iphone", price=5000)
        self.session.add(self.product_a)
        self.session.commit()

    def teardown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_adding_products(self):
        product_from_table = self.session.query(Product).first()
        self.assertIsNotNone(product_from_table)
        self.assertEqual(product_from_table.name, product_from_table.name)
        self.assertEqual(product_from_table.price, product_from_table.price)

    def test_reading_products(self):
        self.session = self.Session()
        self.product_b = Product(name="Galaxy", price=10)
        self.session.add(self.product_b)
        self.session.commit()
        product_form_table = self.session.query(Product).filter_by(name=self.product_b.name).first()
        self.assertEqual(product_form_table.name, self.product_b.name)

    def test_updating_products(self):
        product = self.session.query(Product).first()
        new_price = 2000
        product.price = new_price
        self.session.commit()
        self.assertEqual(product.price, new_price)

    def test_deleting_products(self):
        product = self.session.query(Product).first()
        self.session.delete(product)
        self.session.commit()
        deleted_product = self.session.query(Product).filter_by(id=product.id).first()
        self.assertIsNone(deleted_product)

