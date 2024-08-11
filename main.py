from fastapi import FastAPI

from controller import chat_controller


app = FastAPI()
app.include_router(
    chat_controller.chat_router,
    prefix="/v1",
    tags=["Image"],
)
