from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

class Message(BaseModel):
    text: str

@app.post("/publish")
def publish(message: Message):
    r.publish("MyChannel", message.text)
    return {"status":"success", "message":message.text} #a success message