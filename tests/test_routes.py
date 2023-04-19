import unittest
import sys
import os
from flask import abort, url_for
from flask_testing import TestCase


current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

import run
from extensions import db

class TestBase(TestCase):

    def create_app(self):

        app = run.create_app()
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class RoutesTestCase(TestBase):


    # Ensures that the application instance exists
    def test_app_exists(self):
        self.assertIsNotNone(self.app)

    # Ensures that index page loads correctly
    def test_index(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the index page
    def test_index_data(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'3 Dining' in response.data)

    # Ensures that menu page loads correctly
    def test_menu(self):
        tester = self.app.test_client(self)
        response = tester.get('/menu', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the menu page
    def test_menu_data(self):
        tester = self.app.test_client(self)
        response = tester.get('/menu', content_type='html/text')
        self.assertTrue(b'3 Course Set' in response.data)

    # Ensures that form page loads correctly
    def test_form(self):
        tester = self.app.test_client(self)
        response = tester.get('/form', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the form page
    def test_form_data(self):
        tester = self.app.test_client(self)
        response = tester.get('/form', content_type='html/text')
        self.assertTrue(b'Booking Date' in response.data)

    # Ensures that form accepts only correct input
    def test_form_post_too_many_guests(self):
        tester = self.app.test_client(self)
        response = tester.post('/form', 
        data=dict(book_date='30.08.2021', guests=36, email='john@gmail.com',  follow_redirects=True))
        self.assertIn(b'Sorry, maximum number of guests per day is 30.', response.data)

    # Ensures that form works correctly given valid date, guests number and email
    def test_form_post_weekend(self):
        tester = self.app.test_client(self)
        response = tester.post('/success', 
        data=dict(book_date = '03.09.2021', guests='4', email='mjaro@gmail.com'))
        self.assertIn(b'Thank You for Your Reservation!', response.data)

    # Ensures that admin page loads correctly
    def test_admin(self):
        tester = self.app.test_client(self)
        response = tester.get('/admin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the admin page
    def test_admin_data(self):
        tester = self.app.test_client(self)
        response = tester.get('/admin', content_type='html/text')
        self.assertTrue(b'Enter Booking Date' in response.data)

    # Ensures that result page loads correctly
    def test_result_post_status(self):
        tester = self.app.test_client(self)
        response = tester.post('/result', 
        data=dict(date='31.08.2021',  follow_redirects=True))
        self.assertEqual(response.status_code, 200)

    # Ensures that result page loads correctly given invalid date
    def test_result_post(self):
        tester = self.app.test_client(self)
        response = tester.post('/result', 
        data=dict(date='Tue, 3 Aug 2021 00:00:00 GMT',  follow_redirects=True))
        self.assertIn(b'There are no bookings on the date you have selected!', response.data)

    # Ensures that error/404 page loads correctly
    def test_404(self):
        tester = self.app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensures that the data returned contains actual text from the error/404 page
    def test_404_data(self):
        tester = self.app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertTrue(b'the website you were looking for' in response.data)

    # Ensures that error/500 page loads correctly
    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue(b"An error has occured and we're working to fix the problem." in response.data)



if __name__ == '__main__':
    unittest.main()
