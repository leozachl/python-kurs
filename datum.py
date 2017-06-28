import time
import datetime
from dateutil.relativedelta import relativedelta

print(time.time())

lt = time.localtime()

print(time.strftime("%Y-%m-%dT%H:%M:%S",lt))

#geburtstag = input('Dein Geburtstag: ')

geb = datetime.date(1582,10,15)
dbefore = geb - datetime.timedelta(days = 1)

print(dbefore.Julian)
# diff = datetime.datetime.now() - geb

rdiff = relativedelta(datetime.datetime.now(),geb)

# print(rdiff.years, rdiff.months, rdiff.days, rdiff.hours, rdiff.minutes)

# print (diff.days / 365.25)

#geb = time.strptime(geburtstag, "%d.%m.%Y")

#print(geb)

#gebd = 1966,1,12,0,0,0,0,0,0
#print (time.mktime(gebd))
