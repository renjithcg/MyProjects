import requests
import json


API_URL='https://api.bitbucket.org/2.0/repositories/renjithcg'

Result = requests.get(API_URL,headers={'content-type': 'application/json'},verify=False)
if Result.status_code==200:
    ResultJSON=json.loads(Result.text)
    #print(ResultJSON)
    s=0
    while s<3:
        print(ResultJSON['values'][s]['name'])
        s=s+1

    print(ResultJSON['values'][0]['links']['clone'][-1])
    print(ResultJSON['values'][1]['links']['clone'][-1])
    print(ResultJSON['values'][2]['links']['clone'][-1])
