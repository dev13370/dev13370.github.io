import requests

req = requests.get('https://webscantest.com/')

print(req.headers)