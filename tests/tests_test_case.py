# Django imports
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# App imports
from geo import views
from geo.models import Geolocation
from geo_api import urls


# Establishing fixtures to handle especially expensive setup operations for all of the tests within a module
def setUpModule():
    client = Client()
    user = User.objects.create_user(username='maciej', password='jaroszewski123')
    user.save()
    client.login(username='maciej', password='jaroszewski123')

# Testing create_user view
class CreateUserTest(TestCase):

    def test_create_user_url_is_resolved(self):
        url = reverse('create-user')
        self.assertEquals(resolve(url).func, views.create_user)

    def test_create_user_get(self):
        response = self.client.get(reverse('create-user'))
        self.assertContains(response, 'GEO API', status_code=200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_create_user_post(self):
        data = {
            'username' : 'mjaro',
            'password1' : 'jaroszewski123456',
            'password2' : 'jaroszewski123456'
        }
        response = self.client.post(reverse('create-user'), data, follow=True)
        all_users = User.objects.all()
        self.assertEquals(response.status_code, 401)
        self.assertEquals(all_users.count(), 2)
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)

# Testing geo-detail view
class GeoDetailTest(TestCase):

    def test_geo_detail_url_is_resolved(self):
        url = reverse('geo-detail', args=('100.100.200.11', ))
        self.assertEquals(resolve(url).func, views.geo_detail)

    def test_geo_detail_get_without_authentication(self):
        response = self.client.get(reverse('geo-detail', args=('100.100.200.11', )))
        self.assertEquals(response.status_code, 401)
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)

# Testing geo_create view
class GeoCreate(TestCase):

    def test_geo_create_url_is_resolved(self):
        url = reverse('geo-create')
        self.assertEquals(resolve(url).func, views.geo_create)

    def test_geo_create_get_without_authentication(self):
        response = self.client.get(reverse('geo-create'))
        self.assertEquals(response.status_code, 401)
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)
        
# Testing geo-delete view
class GeoDeleteTest(TestCase):

    def test_geo_delete_url_is_resolved(self):
        url = reverse('geo-delete', args=('100.100.200.11', ))
        self.assertEquals(resolve(url).func, views.geo_delete)

    def test_geo_delete_get_without_authentication(self):
        response = self.client.get(reverse('geo-delete', args=('100.100.200.11', )))
        self.assertEquals(response.status_code, 401)
        self.assertTrue( b'{"detail":"Authentication credentials were not provided."}' in response.content)
        
# Testing Geolocation model
class GeolocationTest(TestCase):

    def test_geolocation_model(self):
        geo = Geolocation(
        ip = '123.456.789',
        longitude = '12,1234567',
        latitude = '56,128976'
        )
        geo.save()
        geo_all = Geolocation.objects.all()
        self.assertIsNotNone(geo)
        self.assertEquals(geo_all.count(), 1)
        self.assertEquals(geo.ip, str(geo))
        
# Testing api_token view
class ApiTokenTest(TestCase):

    def test_api_token_url_is_resolved(self):
        url = reverse('api-token')
        self.assertEquals(resolve(url).func.view_class, urls.TokenObtainPairView)

        
    def test_api_token_post(self):
        data = {
            'username' : 'maciej',
            'password' : 'jaroszewski123'
        }
        response = self.client.post(reverse('api-token'), data)
        self.assertEquals(response.status_code, 200)
        
# Testing api_token_refresh view
class ApiTokenRefresh(TestCase):

    def test_api_token_refresh_url_is_resolved(self):
        url = reverse('api-token-refresh')
        self.assertEquals(resolve(url).func.view_class, urls.TokenRefreshView)









    
