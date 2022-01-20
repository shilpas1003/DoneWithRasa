import requests

url = 'http://localhost:5005/webhooks/rest/webhook'

data = {
    "sender": 1,
    "message": "hii"
}

result = requests.post(url=url, json=data)

print(result.json())


