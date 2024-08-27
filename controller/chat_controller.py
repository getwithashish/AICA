from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse

from client.ai_client import AIClient
from client.openai.openai_client import OpenAIClient
from exceptions import UnauthorizedUserException
from messages import AI_INFERENCE_SUCCESSFUL, USER_NOT_SPECIFIED
from model.chat_request_model import ChatRequestModel
from model.response_model import ResponseModel
from repository.chat_repo import ChatRepo
from repository.mongo.mongo_chat_repo import MongoChatRepo
from repository.mongo.mongo_user_repo import MongoUserRepo
from repository.user_repo import UserRepo
from service.chat_service import ChatService
from util.string_to_uuid_converter import StringToUuidConverter


chat_router = APIRouter()


@chat_router.post("/chat")
async def create_chat(
    chat_request: ChatRequestModel,
    x_user_token: str = Header(None),
    ai_client: AIClient = Depends(OpenAIClient),
    chat_repo: ChatRepo = Depends(MongoChatRepo),
    user_repo: UserRepo = Depends(MongoUserRepo),
):

    chat_id = chat_request.chatId

    if not x_user_token:
        raise UnauthorizedUserException(USER_NOT_SPECIFIED)

    user_id = StringToUuidConverter.convert_to_uuidv5(x_user_token)
    chat_response = await ChatService.initiate_chat(
        user_id=user_id,
        chat_id=chat_id,
        chat_request_messages=chat_request.data,
        ai_client=ai_client,
        chat_repo=chat_repo,
        user_repo=user_repo,
    )

    # TODO The message should be different for ai response and tool
    response = ResponseModel(message=AI_INFERENCE_SUCCESSFUL, data=chat_response.model_dump())
    return JSONResponse(status_code=201, content=response.model_dump())
