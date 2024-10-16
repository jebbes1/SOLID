class NotificationService:
    def send_email(self, message):
        raise NotImplementedError

    def send_sms(self, message):
        raise NotImplementedError

# ISP violation: Forcing implementation of unused methods
class EmailNotification(NotificationService):
    def send_email(self, message):
        print(f"Email: {message}")

# Refactor: Applying ISP
class EmailService:
    def send_email(self, message):
        print(f"Email: {message}")

class SmsService:
    def send_sms(self, message):
        print(f"SMS: {message}")
