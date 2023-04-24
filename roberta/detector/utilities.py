import requests

def get_result(data):

    API_TOKEN = ''
    API_URL = "https://api-inference.huggingface.co/models/roberta-large-openai-detector"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


    output = query({
        "inputs": str(data)
    })

    return output

def get_data(output):
    for element in output[0]:
        if element['label'] == 'LABEL_0':
            label_0 = element['score']
        if element['label'] == 'LABEL_1':
            label_1 = element['score']
    labels = (label_0, label_1)
    return labels
