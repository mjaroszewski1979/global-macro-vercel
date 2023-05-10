import requests
import logging
import os


def get_result(data):
    '''
    This function queries an API to get a result based on the input data.
    :type name: data object
    :param data: contains data in form of text provided by the user

    '''
    # Set API token and URL
    API_TOKEN = os.environ.get('API_KEY')
    API_URL = "https://api-inference.huggingface.co/models/roberta-large-openai-detector"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    # Define a nested function to make a POST request with the API URL and headers
    def query(payload):

        logging.basicConfig(filename='errors.log', format='%(asctime)s %(message)s', level=logging.WARNING)
        
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.warning(e)
        except requests.exceptions.Timeout as e:
            logging.warning(e)
        except requests.exceptions.TooManyRedirects as e:
            logging.warning(e)
        except requests.exceptions.RequestException as e:
            logging.warning(e)
        else:
            return response.json()

    # Send the input data as a payload to the API and return the result
    output = query({
        "inputs": str(data)
    })

    return output


def get_score(result):
    '''
    This function takes a result as input and returns a boolean score based on the label.
    :type name: result object
    :param result: contains response object obtained from Huugingface API

    '''
    # Check if the result object is type of dictionary
    if type(result) == list:
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
