import requests
import os
from dotenv import load_dotenv

import json

# load variables from .env
load_dotenv()

# Access the environment variables
proxycurl_api_key = os.getenv('PROXYCURL_API_KEY')

headers = {'Authorization': 'Bearer ' + proxycurl_api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'url': 'https://www.linkedin.com/in/felix-yang-a61abb135/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

if response.status_code == 200:
    data=response.json()

    with open('linkedin_felixy.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("data has been written into linkdedin_felix.json")
else:
    print(f"failed to fetch data. status code: {response.status_code}")
