# © 2025 @Dypixx.
# Originally developed by @SHARATHITSISME and @ISMARTBOII_UJJWAL
# Modified with additional features and improvements by @Dypixx
# Huge respect to the original creators ❤️

from motor.motor_asyncio import AsyncIOMotorClient
from configs import *

class Database:

    def __init__(self, url, db_name):
        self.db = AsyncIOMotorClient(url)[db_name]
        self.coll = self.db.users

    async def add(self, id):
        if not await self.is_present(id):
            await self.coll.insert_one(dict(id=id, api=None, shortner=None))

    async def is_present(self, id):
        return bool(await self.coll.find_one({'id': int(id)}))
    
    async def set_shortner(self, uid, shortner, api):
        await self.coll.update_one({'id': uid}, {'$set': {'shortner': shortner, 'api': api}})

    async def get_value(self, key, uid):
        user = await self.coll.find_one({'id': uid})
        if user:return user.get(key)

db = Database(DATABASE_URL, "LinkXpert")