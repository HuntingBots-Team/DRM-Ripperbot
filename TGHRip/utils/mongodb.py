import datetime
import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, user):
        return dict(
            id=user.id,
            join_date=datetime.date.today().isoformat(),
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            apply_caption=True,
            upload_as_doc=False,
            thumbnail=None,
            caption=None
        )

    async def add_user(self, user):
        user_data = self.new_user(user)
        await self.col.insert_one(user_data)

    async def is_user_exist(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_apply_caption(self, user_id, apply_caption):
        await self.col.update_one({'id': user_id}, {'$set': {'apply_caption': apply_caption}})

    async def get_apply_caption(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return user.get('apply_caption', True) if user else True

    async def set_upload_as_doc(self, user_id, upload_as_doc):
        await self.col.update_one({'id': user_id}, {'$set': {'upload_as_doc': upload_as_doc}})

    async def get_upload_as_doc(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return user.get('upload_as_doc', False) if user else False

    async def set_thumbnail(self, user_id, thumbnail):
        await self.col.update_one({'id': user_id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return user.get('thumbnail', None) if user else None

    async def set_caption(self, user_id, caption):
        await self.col.update_one({'id': user_id}, {'$set': {'caption': caption}})

    async def get_caption(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return user.get('caption', None) if user else None

    async def get_user_data(self, user_id) -> dict:
        user = await self.col.find_one({'id': int(user_id)})
        return user or None


# Instantiate your database
db = Database(Config.DATABASE_URL, "@urltofile00bot")


# Function to add user if not exists
async def add_user_if_not_exists(user):
    if not await db.is_user_exist(user.id):
        await db.add_user(user)
