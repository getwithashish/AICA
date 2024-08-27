from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from client.mongo.config import DATABASE_NAME, DATABASE_URL
from model.chat_model import ChatModel


class MongoClient:

    async def init():
        client = AsyncIOMotorClient(DATABASE_URL)
        await init_beanie(database=client[DATABASE_NAME], document_models=[ChatModel])
