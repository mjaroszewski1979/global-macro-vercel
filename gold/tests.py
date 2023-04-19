import datetime

# Django imports
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.utils import timezone


# App imports
from .models import Bitcoin
from .views import index, success


# Testing shop app
class GoldTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.bitcoin = Bitcoin(
            title = 'btc-usd',
            dema = 1000,
            ema = 1000,
            ht = 1000,
            kama = 1000,
            sar = 1000,
            sma = 1000,
            trima = 1000,
            wma = 1000,
            date_added = datetime.datetime.now(tz=timezone.utc)
        )
        self.bitcoin.save()


    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Digital Gold |  Home', status_code=200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsNotNone(response.context['bitcoin'])

    def test_index_post(self):
        data={
            'email' : 'mjtrading@gmail.com'
        }
        response = self.client.post(reverse('index'), data, follow=True)
        self.assertContains(response, 'Digital Gold |  Success', status_code=200)
        self.assertTrue(b'Thank you for your email.' in response.content)

    def test_success_url_is_resolved(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func, success)

    def test_success_get(self):
        response = self.client.get(reverse('success'))
        self.assertContains(response, 'Digital Gold |  Success', status_code=200)
        self.assertTemplateUsed(response, 'success.html')

    def test_handler404(self):
        response = self.client.get('/some_url/')
        self.assertContains(response, 'Digital Gold |  Page not found', status_code=404)
        self.assertTemplateUsed(response, '404.html')

    def test_bitcoin_model(self):
        time_now = datetime.datetime.now(tz=timezone.utc)
        btc_obj = Bitcoin(
            title = 'btc-pln',
            dema = 5000,
            ema = 5000,
            ht = 5000,
            kama = 5000,
            sar = 5000,
            sma = 5000,
            trima = 5000,
            wma = 5000,
            date_added = time_now
        )
        btc_obj.save()
        bitcoins = Bitcoin.objects.all()
        btc_obj_print = str(Bitcoin.objects.get(title=btc_obj.title))
        self.assertIsNotNone(btc_obj)
        self.assertEquals(bitcoins.count(), 2)
        self.assertEquals(btc_obj.dema, 5000)
        self.assertEquals(btc_obj.ema, 5000)
        self.assertEquals(btc_obj.ht, 5000)
        self.assertEquals(btc_obj.kama, 5000)
        self.assertEquals(btc_obj.sar, 5000)
        self.assertEquals(btc_obj.sma, 5000)
        self.assertEquals(btc_obj.trima, 5000)
        self.assertEquals(btc_obj.wma, 5000)
        self.assertEquals(btc_obj.date_added, time_now)
        self.assertEquals(btc_obj_print, str(btc_obj.title))


