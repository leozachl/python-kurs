class WifiMessage:

    @property
    def body(self):
        return self.body

    @property
    def subject(self):
        return self.subject

    def print(self):
        print(self.body)

class SMS(WifiMessage):

    def __init__(self, phone_number = ''):
        self.__phone_number = phone_number

    @property
    def phone_number(self):
        return self.__phone_number

class MyEmail(WifiMessage):

    @property
    def email_address(self):
        return self.email_address