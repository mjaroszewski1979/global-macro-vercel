import requests
import time
import os

# This function queries an API to get a result based on the input data
def get_result(data):
    # Set API token and URL
    API_TOKEN = os.environ.get('API_KEY')
    API_URL = "https://api-inference.huggingface.co/models/roberta-large-openai-detector"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    # Define a nested function to make a POST request with the API URL and headers
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    # Send the input data as a payload to the API and return the result
    output = query({
        "inputs": str(data)
    })

    return output

# This function takes a result as input and returns a boolean score based on the label
def get_score(result):
    # Iterate through the first element in the result list
    if type(result) == dict:
        time.sleep(20)

    else:
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
