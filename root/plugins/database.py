import datetime
import motor.motor_asyncio


class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            generate_ss=False,
            generate_sample_video=False
        )
    async def get_generate_ss(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('generate_ss', True)

    async def set_generate_sample_video(self, id, generate_sample_video):
        await self.col.update_one({'id': id}, {'$set': {'generate_sample_video': generate_sample_video}})

    async def get_generate_sample_video(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('generate_sample_video', True)
