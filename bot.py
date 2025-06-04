from pyrogram.client import Client
from configs import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ShortnerBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "Modules"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"::==>> Dypixx Tech <<==::\n┈━═☆ {me.first_name} ☆═━┈")

    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        print(f"{me.first_name} is stopped...")

bot = Bot()