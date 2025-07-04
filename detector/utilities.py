import requests
import logging
import os


def get_result(data):
    '''
    This function queries an API to get a result based on the input data.
    :type name: data object
    :param data: contains data in form of text provided by the user

    '''
    # Set API HF TOKEN and URL
    API_TOKEN = os.environ.get('HF_TOKEN')
    API_URL = "https://router.huggingface.co/hf-inference/models/openai-community/roberta-large-openai-detector"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    # Define a nested function to make a POST request with the API URL and headers
    def query(payload):
        """
        Sends a query payload to the API and returns the response in JSON format.
        Args:
            payload (dict): The query payload to be sent to the API.  
        Returns:
            dict: The response from the API in JSON format.
        """
        # Configure logging settings
        logging.basicConfig(filename='errors.log', format='%(asctime)s %(message)s', level=logging.WARNING)
        
        try:
            # Send the request to the API
            response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
            # Check for any HTTP errors in the response
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Log HTTP errors as warnings
            logging.warning(e)
        except requests.exceptions.Timeout as e:
            # Log Timeout errors as warnings
            logging.warning(e)
        except requests.exceptions.TooManyRedirects as e:
            # Log TooManyRedirects errors as warnings
            logging.warning(e)
        except requests.exceptions.RequestException as e:
            # Log any other RequestException errors as warnings
            logging.warning(e)
        else:
            # Return the response in JSON format
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
