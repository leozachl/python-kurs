import re


addr = "Promenadegasse 22/1/3, 1170 Wien, AUSTRIA"

data = re.search (r'(.*?),\s*(\d{4})\s*(.*?)(?:,\s(.*))?$', addr)

if data:
    print (data.groups())