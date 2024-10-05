from service import Service


class Telegramdel2(Service):
    async def run(self):
        await self.post(
            "https://my.telegram.org/auth?to=delete",
            data={"phone": "+" + self.formatted_phone},
        )
