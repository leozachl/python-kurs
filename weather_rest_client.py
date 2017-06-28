import requests
from pprint import pprint

weather_url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'

response = requests.get(weather_url)
data = response.json()

# pprint(data)

if 'main' in data and 'name' in data :
    if 'temp' in data['main']:
        print('Die aktuelle Temeratur in %s ist %.1f°C' % (data['name'], data['main']['temp'] - 273.15 ))