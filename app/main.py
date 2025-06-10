from fastapi import FastAPI

from .routers.chat import chat
from .routers.manual import manual

app = FastAPI()

app.include_router(chat.router)
app.include_router(manual.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
