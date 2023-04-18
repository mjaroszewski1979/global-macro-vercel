# Django imports
from django.contrib.auth.models import User
from django.urls import reverse

# Rest framework imports
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase

# App imports
from geo.models import Geolocation

# Creating parent test class that inherits from APITestCase 
class TestCaseBase(APITestCase):
    @property
    def bearer_token(self):
        username = 'mjaro1245'
        password = 'jaroszewski987'
        # Instantiating client to make requests for testing purposes
        client = APIClient()
        url = reverse('api-token')
        # Creating and saving test user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        # Using client to login new user
        self.client.login(username=username, password=password)
        # Sending a post request to acquire access token
        resp = client.post(url, {'username': username, 'password': password}, format='json')
        token = resp.data['access']
        return {"HTTP_AUTHORIZATION":f'Bearer {token}'}

class TestGeoAPI(TestCaseBase):
    
    # Using setUp method to define instructions that will be executed before and after each test
    def setUp(self):
        self.geo = Geolocation(
            ip = '134.201.250.155',
            longitude = '12,1234567',
            latitude = '56,128976'
        )
        self.geo.save()

    # Testing geo_detail endpoint with valid credentials
    def test_get_geo_detail(self):
        url = reverse('geo-detail', args=(self.geo.ip, ))
        response = self.client.get(url, **self.bearer_token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.geo.ip in response.data['ip'])
    
    # Testing geo_delete endpoint with valid credentials
    def test_delete_geo(self):
        url = reverse('geo-delete', args=(self.geo.ip, ))
        response = self.client.get(url, **self.bearer_token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals({'Succes': 'Geolocation succsesfully deleted!'}, response.data)
    
    # Testing geo_create endpoint with valid credentials
    def test_create_geo(self):
        data = {"ip" : "109.173.214.104"}
        url = reverse('geo-create')
        response = self.client.post(url, data, **self.bearer_token)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue('Geolocation added!' in response.data)











