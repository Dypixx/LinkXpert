# © 2025 @Dypixx.
# Originally developed by @SHARATHITSISME and @ISMARTBOII_UJJWAL
# Modified with additional features and improvements by @Dypixx
# Huge respect to the original creators ❤️

from typing import Any
from configs import *
from motor import motor_asyncio
from datetime import datetime, timedelta
client: motor_asyncio.AsyncIOMotorClient[Any] = motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
MT = client["DypixxLinkXpert"]

class dypixx:
    def __init__(self):
        self.users = MT["users"]
        self.banned_users = MT["banned_users"]
        self.cache: dict[int, dict[str, Any]] = {}

    async def addUser(self, user_id: int, name: str) -> dict[str, Any] | None:

        try:
            user: dict[str, Any] = {"user_id": user_id, "name": name}
            await self.users.insert_one(user)
            self.cache[user_id] = user
            return user
        except Exception as e:
            print("Error in addUser: ", e)

    async def get_user(self, user_id: int) -> dict[str, Any] | None:
        try:
            if user_id in self.cache:
                return self.cache[user_id]
            user = await self.users.find_one({"user_id": user_id})
            return user
        except Exception as e:
            print("Error in getUser: ", e)
            return None

    async def get_all_users(self) -> list[dict[str, Any]]:
        try:
            users: list[dict[str, Any]] = []
            async for user in self.users.find():
                users.append(user)
            return users
        except Exception as e:
            print("Error in getAllUsers: ", e)
            return []

    async def ban_user(self, user_id: int, reason: str = None) -> bool:
        try:
            ban_dypixx = {
                "user_id": user_id,
                "reason": reason
            }
            await self.banned_users.insert_one(ban_dypixx)
            return True
        except Exception as e:
            print("Error in banUser: ", e)
            return False

    async def unban_user(self, user_id: int) -> bool:
        try:
            result = await self.banned_users.delete_one({"user_id": user_id})
            return result.deleted_count > 0
        except Exception as e:
            print("Error in unbanUser: ", e)
            return False

    async def is_user_banned(self, user_id: int) -> bool:
        try:
            user = await self.banned_users.find_one({"user_id": user_id})
            return user is not None
        except Exception as e:
            print("Error in isUserBanned: ", e)
            return False


dy = dypixx()
