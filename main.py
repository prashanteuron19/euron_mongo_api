from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv  

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
Client = AsyncIOMotorClient(MONGO_URI)
db = Client["euron"]
euron_data = db["euron_coll"]

app = FastAPI()

class EuronData(BaseModel):
    name: str
    phone: int
    city: str
    Course: str

@app.post("/euron/insert")
async def euron_data_insert_helper(data:EuronData):
    result =await euron_data.insert_one(data.dict())
    return str(result.inserted_id)