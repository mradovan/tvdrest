import json
import requests
import pprint
url = 'https://apex.oracle.com/pls/apex/kazaliste/postme/testme/'
data = {"MID" : "OTEMP", "VAL": 12.9}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())
