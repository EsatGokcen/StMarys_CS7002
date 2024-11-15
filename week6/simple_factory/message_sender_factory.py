from abc import staticmethod
from concrete_msg_sndrs import *

class MessageSenderFactory:

    @staticmethod
    def create_message_sender(channel):
        if channel == 'email':
            return EmailSender()
        elif channel == 'sms':
            return SMSSender()
        elif channel == 'push':
            return PushNotificationSender()
        else:
            raise ValueError('Invalid communication channel')

