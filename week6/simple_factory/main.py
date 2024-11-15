from message_sender_factory import MessageSenderFactory

def main():

    factory = MessageSenderFactory()

    email_sender = factory.create_message_sender('email')
    email_sender.send_message("This is an email message")

    sms_sender = factory.create_message_sender('sms')
    sms_sender.send_message("This is an SMS message")

    push_sender = factory.create_message_sender('push')
    push_sender.send_message("This is a push notification message")

if __name__ == '__main__':
    main()
