import requests
import os

class Detector:
    def __init__(self):
        self.api_token = os.environ.get('API_KEY')
        self.api_url = "https://api-inference.huggingface.co/models/roberta-large-openai-detector"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
    
    def get_result(self, data):

        payload = dict(inputs = str(data))

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
        
    def get_score(self, result):

    # Check if the result object is type of dictionary
        if len(result[0]) == 2:
            # Iterate through the first element in the result list
            for element in result[0]:
                # Check if the label is 'LABEL_0'
                if element['label'] == 'LABEL_0':
                    label_0 = element['score']
                    # If the score for 'LABEL_0' is greater than 0.5, return False
                    if label_0 > 0.5:
                        return False
                    # Otherwise, return True
                    else:
                        return True
        else:
            return 'Error'
