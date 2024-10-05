from service import Service


class Telegram(Service):
    def send_sms(self):
        self.session.post('https://my.telegram.org/auth/send_password', data={'phone': '+' + self.formatted_phone})
