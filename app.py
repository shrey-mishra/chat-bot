from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat_bot import send_message_and_get_response

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/test")
async def test():
    return "Hello World!"


@app.get("/api/chat")
async def chat(message: str = ""):
    return send_message_and_get_response(message)
