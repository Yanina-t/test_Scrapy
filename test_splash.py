import requests

url = 'https://xn--80az8a.xn--d1aqf.xn--p1ai/сервисы/каталог-новостроек/список-объектов/список?place=0-6'
splash_url = 'http://localhost:8050/render.html'

response = requests.get(splash_url, params={'url': url, 'wait': 2})

print(response.text)
