import requests

url="https://www.googl.com/"

resp = requests.get(url)
print(resp.text)