import requests

API_TOKEN = ''
API_URL = "https://api-inference.huggingface.co/models/roberta-large-openai-detector"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

data = '''
'''
output = query({
    "inputs": data
})