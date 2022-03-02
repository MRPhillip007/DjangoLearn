import requests

url = 'http://127.0.0.1:8000/generic/article/12/'
headers = {
    "User-Agent": "Google Chrome",
    "Content-Type": "application/json",
    "Authorization": "Token adf9b556e6f3583ba8282dea3104ab0fab97d972"
}

for _ in range(10000):
    requests.get(url, headers=headers)

print('Complete')