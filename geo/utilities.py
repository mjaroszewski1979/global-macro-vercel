import os
import requests
from .models import Geolocation

def get_geo(ip, api_key = os.environ.get('API_KEY')):
    '''
    This function is using requests and calling an external api service to extract geolocation data for a given ip address
            Parameters:
                    ip (str): A valid ip address
            Returns:
                    message (json): Success or error message depending on user input and response status codes 
    '''
    fields = 'longitude,latitude,ip'
    response = requests.get('http://api.ipstack.com/' + str(ip) + '?access_key=' + str(api_key) + '&fields=' + fields)
    response_json = response.json()
    if response.status_code == 200:
        if response_json.get('ip') != None:
            longitude = response_json.get('longitude')
            latitude = response_json.get('latitude')
            success_msg = { 'Success' : 'Geolocation added!' }
            new_geo = Geolocation.objects.create(ip=str(ip), longitude=longitude, latitude=latitude)
            new_geo.save()
            return success_msg
        else:
            error_msg = response_json
            return error_msg
    else:
        return response.status_code
