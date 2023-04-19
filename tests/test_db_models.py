import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

import run
from models import Date, Details
from extensions import db

app = run.create_app()
app.config['TESTING'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db.init_app(app)
app.app_context().push() 


class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Ensures that data base models are working correctly
    def test_db_models(self):
        new_book_date = Date(book_date='2021-09-04', guests_total=5)
        new_detail = Details(email='john@gmail.com', guests=5, date=new_book_date)
        db.session.add(new_book_date)
        db.session.commit()
        db.session.add(new_detail)
        db.session.commit()
        existing_date = Date.query.filter_by(book_date='2021-09-04').first()
        existing_detail = Details.query.filter_by(date_id=existing_date.id).first()
        self.assertEqual(existing_date.guests_total, 5)
        self.assertEqual(existing_detail.email, 'john@gmail.com')

if __name__ == '__main__':
    unittest.main()

