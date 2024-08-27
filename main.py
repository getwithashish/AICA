from fastapi import FastAPI

from client.mongo.mongo_client import MongoClient
from controller import chat_controller
from controller import exception_handler


# TODO Use Logging

app = FastAPI(
    title="Chatbot Backend Server",
    on_startup=[
        MongoClient.init,
    ],
)
app.include_router(
    chat_controller.chat_router,
    prefix="/v1",
    tags=["Image"],
)

exception_handler.include_exception_handler_in_app(app=app)
