import argparse, re

## komplexere Parameteruebergabe zB mit
## https://pypi.python.org/pypi/ConfigArgParse


parser = argparse.ArgumentParser()

parser.add_argument('-i', '--inputfile',
  action="store", dest="inputfile",
  help="inputfile to be parsed")
parser.add_argument('-d', '--debug',
  help="debug")

options = parser.parse_args()

print ('Input File', options.inputfile)


with open(options.inputfile, "r") as file:
  lines = file.readlines()

# Allianz Europe Equity Growth Fund
# LU0256839191 / Aktien    Rating 5 Sterne        Ja      12,54%/ 8,67%/ 1,26%    12,68%/ 14,44%/ 13,49%

i = 0
for line in lines: 
#  print('*** ', i)
  line = line.rstrip()
  i += 1
  if i > 10 and options.debug:
    break
  m = re.match( r'Aktion wählen', line ) 
  if m:
    continue
#print(line)
  data = re.search(r'^(\w\w.+?) /.*Rating (\d) Sterne.*?([-\d].*)', line)
  if data:
    # print(data.group(3))
    p = re.split(r'[\s\/\%]+', data.group(3))
    print( '{};{};'.format(data.group(1), data.group(2) ),  ';'.join(p).replace(',', '.'))
  else: 
    print(line,';', end="")
