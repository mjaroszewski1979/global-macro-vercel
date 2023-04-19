import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

import run
from models import InfoForm


app = run.create_app()


class RoutesTestCase(unittest.TestCase):

    # Ensures that form model works correctly
    def test_new_form(self):
        with app.test_request_context():
            form = InfoForm(book_date= '2021-08-31', guests=5, email='john@gmail.com')
            self.assertEqual(form.book_date.data, '2021-08-31')
            self.assertEqual(form.guests.data, 5)
            self.assertEqual(form.email.data, 'john@gmail.com')

    # Ensures that form model validator returns errors
    def test_new_form_weekend(self):
        with app.test_request_context():
            form = InfoForm(book_date= '2021-09-04', guests=5, email='john@gmail.com')
            self.assertNotEqual(form.errors, None)

  


if __name__ == '__main__':
    unittest.main()