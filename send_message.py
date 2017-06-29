'''
def send_email(message, email_address):
    return 0

def send_sms(message, phone_number):
    return 0

send_email()

send_sms()
'''

from WifiMessage import SMS, MyEmail
from pprint import pprint

sms = SMS

sms.body.setter('World')
sms.subject = 'Title'
# sms.phone_number = '0677 624'

email = MyEmail
email.email_address = 'leo@zachl.net'

sms.print()
print (sms.phone_number)
print(email.email_address)
