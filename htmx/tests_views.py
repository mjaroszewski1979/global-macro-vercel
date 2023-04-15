from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView

# App imports
from .models import Car, UserCars, User
from . import views

class ViewsTest(TestCase):
    '''
    This class will include test methods neccessary to check if views.py file
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

    def test_index_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, views.HomeView)

    def test_index_get(self):
        """
        This is test method to verify if acquired response to a get request has correct status code,
        html title content and uses appropriate template.
        """
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'My Rides | Home Page', status_code=200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, views.RegisterView)

    def test_register_get(self):
        """
        This is test method to verify if acquired response to a get request has correct status code,
        html title content and uses appropriate template.
        """
        response = self.client.get(reverse('register'))
        self.assertContains(response, 'My Rides | Register', status_code=200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_post(self):
        """
        This is test method to verify if acquired response to a post request has correct status code,
        html title content and uses appropriate template.
        """
        data={
            'username' : 'maciej123',
            'password1' : 'jaroszewski',
            'password2' : 'jaroszewski'
        }
        response = self.client.post(reverse('register'), data, follow=True)
        self.assertContains(response, 'My Rides | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, views.Login)

    def test_login_get(self):
        """
        This is test method to verify if acquired response to a get request has correct status code,
        html title content and uses appropriate template.
        """
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'My Rides | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_post(self):
        """
        This is test method to verify if acquired response to a post request has correct status code,
        html title content and uses appropriate template.
        """
        data={
            'username' : 'testuser',
            'password' : '1235'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertContains(response, 'My Rides | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_car_list_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        self.client.force_login(user=self.user)
        url = reverse('car_list')
        self.assertEquals(resolve(url).func.view_class, views.CarList)

    def test_car_list_get_authenticated_user(self):
        """
        This is test method to verify if acquired response to a get request made by authenticated user
        has correct status code, html title content and uses appropriate template.
        """
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('car_list'))
        self.assertContains(response, 'My Rides | Cars List', status_code=200)
        self.assertTemplateUsed(response, 'cars.html')

    def test_car_list_get_anonymous_user(self):
        """
        This is test method to verify if acquired response to a get request has correct status code.
        """
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 302)


    def test_car_list_context(self):
        """
        This is test method to verify if acquired response to a get request made by authenticated user
        has correct context dictionary passed to the template.
        """
        self.client.force_login(user=self.user)
        UserCars.objects.create(user=self.user, car=self.car, order=1)
        response = self.client.get(reverse('car_list'))
        ctx_car = response.context['cars'].get()
        self.assertIsNotNone(response.context['cars'])
        self.assertEqual(ctx_car.car.producer, 'porshe')

