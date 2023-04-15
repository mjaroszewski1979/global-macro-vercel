import io
from PIL import Image

from django.test import TestCase, Client
from django.urls import reverse, resolve

# App imports
from .models import Car, UserCars, User
from . import htmx_views


def generate_photo_file():
    '''
    This function will return an artificial image for testing purposes.
    '''
    file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file

class HtmxViewsTest(TestCase):
    '''
    This class will include test methods neccessary to check if htmx_views.py file
    behaves as expected.
    '''

    def setUp(self):
        """
        This method is called before every test function to set up any objects
        neccessary to perform a specified task. 
        """
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.car = Car.objects.create(producer='porshe')
        self.car.save()


    def tearDown(self):
        """
        This method is called after every test function to delete existing objects
        neccessary to perform a specified task. 
        """
        self.user.delete()
        self.car.delete()

    def test_check_username_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('check-username')
        self.assertEquals(resolve(url).func, htmx_views.check_username)

    def test_check_username_post_existing_username(self):
        """
        This is test method to verify if acquired response to a post request has correct status code
        and returns the expected content.
        """
        data={
            'username' : 'testuser'
        }
        response = self.client.post(reverse('check-username'), data)
        self.assertEqual(response.content, b'This username already exists')
        self.assertEqual(response.status_code, 200)

    def test_check_username_post_new_username(self):
        """
        This is test method to verify if acquired response to a post request has correct status code
        and returns the expected content.
        """
        data={
            'username' : 'newuser'
        }
        response = self.client.post(reverse('check-username'), data)
        self.assertEqual(response.content, b'This username is available')
        self.assertEqual(response.status_code, 200)

    def test_add_car_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('add_car')
        self.assertEquals(resolve(url).func, htmx_views.add_car)

    def test_add_car_post_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        data = {
            'car_producer' : 'audi'
        }
        response = self.client.post(reverse('add_car'), data)
        self.assertEqual(response.status_code, 302)

    def test_add_car_post_authenticated_user(self):
        """
        This is test method to verify if acquired response to a post request made by authenticated user:
        - has the expected context dictionary passed to the template
        - returns correct status code
        - uses appropriate template
        """
        data = {
            'car_producer' : 'audi'
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse('add_car'), data)
        self.assertEqual(response.status_code, 200)
        ctx_car_producer = response.context['cars'].get()
        self.assertIsNotNone(response.context['cars'])
        self.assertEqual(ctx_car_producer.car.producer, 'audi')
        self.assertTemplateUsed(response, 'partials/car_list.html')

    def test_delete_car_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('delete_car', args= (1, ))
        self.assertEquals(resolve(url).func, htmx_views.delete_car)

    def test_delete_car_get_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        response = self.client.get(reverse('delete_car', args= (1, )))
        self.assertEqual(response.status_code, 302)

    def test_delete_car_get_authenticated_user(self):
        """
        This is test method to verify if acquired response to a delete request has:
        -  correct status code 
        - returns expected number of UserCars instances
        - response has the expected context dictionary passed to the template
        - view function is using accurate template
        """
        data = {
            'car_producer' : 'audi'
        }
        self.client.force_login(user=self.user)
        self.client.post(reverse('add_car'), data)
        response = self.client.delete(reverse('delete_car', args= (1, )))
        num_cars = UserCars.objects.filter(user=self.user).count()
        ctx = response.context['cars']
        self.assertEqual(num_cars, 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/car_list.html')
        self.assertIsNotNone(ctx)
        self.assertEqual(str(ctx), '<QuerySet []>')
        
    def test_search_car_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('search_car')
        self.assertEquals(resolve(url).func, htmx_views.search_car)

    def test_search_car_post_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        data = {
            'search' : 'porshe'
        }
        response = self.client.post(reverse('search_car'), data)
        self.assertEqual(response.status_code, 302)

    def test_search_car_post_authenticated_user(self):
        """
        This is test method to verify if:
        - acquired response to a delete request has correct status code 
        - returns expected number of UserCars instances
        - response has the expected context dictionary passed to the template
        - view function is using accurate template
        """
        data = {
            'search' : 'porshe'
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse('search_car'), data)
        self.assertEqual(response.status_code, 200)
        ctx_car_producer = response.context['results'].get()
        self.assertIsNotNone(response.context['results'])
        self.assertEqual(ctx_car_producer.producer, 'porshe')
        self.assertTemplateUsed(response, 'partials/search_results.html')

    def test_detail_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('detail', args= (1, ))
        self.assertEquals(resolve(url).func, htmx_views.detail)

    def test_detail_get_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        response = self.client.get(reverse('detail', args= (1, )))
        self.assertEqual(response.status_code, 302)

    def test_detail_get_authenticated_user(self):
        """
        This is test method to verify if acquired response to a get request made by authenticated user:
        - has the expected context dictionary passed to the template
        - returns correct status code
        - uses appropriate template
        """
        data = {
            'car_producer' : 'audi'
        }
        self.client.force_login(user=self.user)
        self.client.post(reverse('add_car'), data)
        response = self.client.get(reverse('detail', args= (1, )))
        user_car = response.context['user_car']
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(user_car)
        self.assertEqual(user_car.car.producer, 'audi')
        self.assertTemplateUsed(response, 'partials/car_detail.html')

    def test_cars_partial_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('car_list_partial')
        self.assertEquals(resolve(url).func, htmx_views.cars_partial)

    def test_cars_partial_get_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        response = self.client.get(reverse('car_list_partial'))
        self.assertEqual(response.status_code, 302)

    def test_cars_partial_get_authenticated_user(self):
        """
        This is test method to verify if acquired response to a get request made by authenticated user:
        - has the expected context dictionary passed to the template
        - returns correct status code
        - uses appropriate template
        """
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('car_list_partial'))
        ctx = response.context['cars']
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(ctx)
        self.assertTemplateUsed(response, 'partials/car_list.html')


    def test_upload_photo_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('upload_photo', args= (1, ))
        self.assertEquals(resolve(url).func, htmx_views.upload_photo) 

    def test_upload_photo_post_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        response = self.client.post(reverse('upload_photo', args= (1, )))
        self.assertEqual(response.status_code, 302)

    def test_upload_photo_post_authenticated_user(self):
        """
        This is test method to verify if acquired response to a post request made by authenticated user:
        - has the expected context dictionary passed to the template
        - returns correct status code
        - uses appropriate template
        """
        image = {
            'photo' : generate_photo_file()
        }
        data = {
            'car_producer' : 'audi'
        }
        self.client.force_login(user=self.user)
        self.client.post(reverse('add_car'), data)
        response = self.client.post(reverse('upload_photo', args= (1, )), image)
        user_car = response.context['user_car']
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(user_car)
        self.assertTemplateUsed(response, 'partials/car_detail.html')


    def test_clear_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('clear')
        self.assertEquals(resolve(url).func, htmx_views.clear)

    def test_clear_get(self):
        """
        This is test method to verify if acquired response to a get request has correct status code.
        """
        response = self.client.get(reverse('clear'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')

    def test_sort_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('sort')
        self.assertEquals(resolve(url).func, htmx_views.sort)

    def test_sort_get(self):
        """
        This is test method to verify if acquired response to a get request has correct status code and
        uses appropriate template.
        """
        self.client.force_login(user=self.user)
        self.client.post(reverse('add_car'), {'car_producer' : 'audi'})
        self.client.post(reverse('add_car'), {'car_producer' : 'skoda'})
        cars = UserCars.objects.filter(user=self.user)
        for car in cars:
            car_order = {
                car.order : car.car.producer
            }
        response = self.client.post(reverse('sort'), car_order)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/car_list.html')




        


