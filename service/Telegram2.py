from service import Service


class Telegram2(Service):
    async def run(self):
        await self.client.post(
            "https://my.telegram.org/auth/send_password",
            data={
                "msisdn": self.formatted_phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763",
            },
        )
