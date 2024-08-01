import unittest
from sqlalchemy import create_engine
from models import Base, Users
from sqlalchemy.orm import sessionmaker


class TestUser(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.test_user = Users(name="TestUser", email="test@gmail.com")
        self.session.add(self.test_user)
        self.session.commit()

    def teardown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_user_in_table_by_email(self):
        user_from_table = self.session.query(Users).filter_by(email=self.test_user.email).first()
        self.assertIsNotNone(user_from_table)
        self.assertEqual(user_from_table.email, self.test_user.email)

    def test_user_in_table_by_name(self):
        user_from_table = self.session.query(Users).filter_by(name=self.test_user.name).first()
        self.assertIsNotNone(user_from_table)
        self.assertEqual(user_from_table.name, self.test_user.name)
