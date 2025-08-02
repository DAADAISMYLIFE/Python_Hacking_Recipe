import requests

url = "https://hakhub.net"
r = requests.get(url)
print(f"Status Code : {r.status_code}")
print(f"Response Header : {r.headers}")
print(f"Response Body")
print(r.text[:1000])