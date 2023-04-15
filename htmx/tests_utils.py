from django.test import TestCase, Client
from django.urls import reverse

# App imports
from .models import Car, UserCars, User
from .utils import get_max_order, reorder


class UtilsTest(TestCase):

    def setUp(self):
        """
        This method is called before every test function to set up any objects
        neccessary to perform a specified task. 
        """
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.porshe = Car.objects.create(producer='porshe')
        self.porshe.save()
        self.audi = Car.objects.create(producer='audi')
        self.audi.save()


    def tearDown(self):
        """
        This method is called after every test function to delete existing objects
        neccessary to perform a specified task. 
        """
        self.user.delete()
        self.porshe.delete()
        self.audi.delete()

    def test_get_max_order_existing_cars(self):
        """
        This is test method to verify if get_max_order function returns
        expected value when as an input we pass logged-in user object with
        existing cars attached to it.
        """
        self.client.force_login(user=self.user)
        UserCars.objects.create(user=self.user, car=self.porshe, order=1)
        UserCars.objects.create(user=self.user, car=self.audi, order=2)
        result = get_max_order(self.user)
        self.assertEqual(result, 3)

    def test_get_max_order_no_cars(self):
        """
        This is test method to verify if get_max_order function returns
        expected value when as an input we pass logged-in user object without
        existing cars attached to it.
        """
        self.client.force_login(user=self.user)
        result = get_max_order(self.user)
        self.assertEqual(result, 1)

    def test_reorder_existing_cars(self):
        """
        This is test method to verify if reorder function returns
        expected value when as an input we pass logged-in user object with
        existing cars attached to it.
        """
        self.client.force_login(user=self.user)
        UserCars.objects.create(user=self.user, car=self.porshe, order=1)
        UserCars.objects.create(user=self.user, car=self.audi, order=2)
        self.client.delete(reverse('delete_car', args= (1, )))
        audi = UserCars.objects.filter(order=1).get()
        self.assertEqual(audi.order, 1)

    def test_reorder_no_cars(self):
        """
        This is test method to verify if reorder function returns
        expected value when as an input we pass logged-in user object without
        existing cars attached to it.
        """
        self.client.force_login(user=self.user)
        result = reorder(self.user)
        self.assertEqual(result, None)



    