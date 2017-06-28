import requests
from pprint import pprint

url = 'https://finance.yahoo.com/d/quotes.csv?s=EBS.VI&f=snl1hg'

response = requests.get(url)
data = response.text
pprint(data)