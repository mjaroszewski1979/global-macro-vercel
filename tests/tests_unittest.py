# python imports
import unittest
import os

# app imports
from geo.utilities import get_geo

# Testing get_geo function
class TestGetGeo(unittest.TestCase):

    def test_get_geo_valid_ip(self):
        actual = get_geo('134.201.250.155', os.environ.get('API_KEY'))
        expected = {'Success': 'Geolocation added!'}
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_ip(self):
        actual = get_geo('12',  os.environ.get('API_KEY'))
        expected = {'success': False,
                    'error': {'code': 106,
                    'type': 'invalid_ip_address',
                    'info': 'The IP Address supplied is invalid.'}}
        self.assertEquals(actual, expected)

    def test_get_geo_invalid_api_key(self):
        actual = get_geo('134.201.250.155', 'invalid')
        expected = {'success': False,
                    'error': {'code': 101,
                    'type': 'invalid_access_key',
                    'info': 'You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]'}}
        self.assertEquals(actual, expected)
