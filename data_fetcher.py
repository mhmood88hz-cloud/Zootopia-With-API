import dotenv
import requests
import os
from dotenv import load_dotenv
from pygments.lexers import python

load_dotenv()
API_KEY = os.getenv('API_KEY')
def fetch_data(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {
        "X-Api-Key": API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()