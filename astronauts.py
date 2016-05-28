import requests

url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
j = r.json()
n = j['number']
print(n)
