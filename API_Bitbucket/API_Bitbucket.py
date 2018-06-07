import requests
import json


API_URL='https://api.bitbucket.org/2.0/repositories/renjithcg'

Result = requests.get(API_URL)

if Result.status_code==200:
    ResultJSON = json.loads(Result.text)
    for obj in ResultJSON['values']:
        print(obj['name'])

    for url in ResultJSON['values']:
        print(url['links']['clone'][-1]['href'])

   
