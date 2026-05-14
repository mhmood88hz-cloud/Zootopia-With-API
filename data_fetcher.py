import requests

API_KEY = "plyPimnA2MNAWv7ULhuqD8BQVc4tjcM3sQAzEqYR"

def fetch_data(animal_name):
  url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

  headers = {"X-Api-Key": API_KEY}

  response = requests.get(url, headers=headers)

  return response.json()