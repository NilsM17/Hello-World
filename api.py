import requests

api_key = '00e29323d5c24fc6d5f314a1f7a89265'
city = 'Emsbueren'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=de&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    wetter = data['weather'][0]['description']
    temp = data['main']['temp']
else:
    data = response.status_code

print(data)
print("-" * 50)
print(wetter)
print(temp)