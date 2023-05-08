import requests
import time
import os

class Detector:
    def __init__(self, data):
        self.data = data
        self.api_token = os.environ.get('API_KEY')
        self.api_url = "https://api-inference.huggingface.co/models/roberta-large-openai-detector"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
    
    def get_result(self):
        '''
        This function queries an API to get a result based on the input data.
        :type name: data object
        :param data: contains data in form of text provided by the user

        '''

        # Define a nested function to make a POST request with the API URL and headers
        def query(payload):
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(e)
            except requests.exceptions.Timeout as e:
                print(e)
            except requests.exceptions.TooManyRedirects as e:
                print(e)
            except requests.exceptions.RequestException as e:
                print(e)
            else:
                return response.json()

        # Send the input data as a payload to the API and return the result
        output = query({
            "inputs": str(self.data)
        })

        return output