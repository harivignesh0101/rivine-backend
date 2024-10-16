import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()  # Load environment variables from .env file

print(os.getenv("MONGO_URI"))
class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")

settings = Settings()

# Initialize MongoDB connection
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
