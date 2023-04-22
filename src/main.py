from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import Message
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/get/")
async def get():
    return {'message': 'Hello!', 'method': 'GET <OK>'}

@app.post("/api/post/")
async def post(data: Message):
    print(data.message)
    return {'data': data.dict(), 'method': 'POST <OK>'}
