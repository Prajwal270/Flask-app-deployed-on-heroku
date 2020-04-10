import requests
url = 'http://localhost:70/predict_api'
r = requests.post(url,json{'first':5.1,'second':3.0, 'third':2.1,'forth':3.8})

print(r.json())