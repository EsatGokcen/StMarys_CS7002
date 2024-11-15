from message_sender import MessageSender

class EmailSender(MessageSender):
    def send_message(self, message):
        print(f'Sending email: {message}')

class SMSSender(MessageSender):
    def send_message(self, message):
        print(f'Sending sms message: {message}')

class PushNotificationSender(MessageSender):
    def send_message(self, message):
        print(f'Sending push notification: {message}')