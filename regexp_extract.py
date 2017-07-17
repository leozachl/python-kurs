import re


addr = "Promigasse 1/1/1, 1010 Wien, AUSTRIA"

data = re.search (r'(.*?),\s*(\d{4})\s*(.*?)(?:,\s(.*))?$', addr)

if data:
    print (data.groups())
