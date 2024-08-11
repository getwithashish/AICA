from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse

from client.ai_client import AIClient
from client.openai.openai_client import OpenAIClient
from model.chat_request_model import ChatRequestModel
from model.response_model import ResponseModel
from service.chat_history_service import ChatHistoryService
from service.chat_service import ChatService


chat_router = APIRouter()


@chat_router.get("/chat/list")
async def get_chat_list(offset: int = 0):
    chat_list = {
        "message": "Successfully fetched the chat list",
        "data": {
            "total": 20,
            "limit": 10,
            "chats": [
                {
                    "id": 10,
                    "chatTitle": "Raising a ticket with SFM",
                    "timestamp": "2017-07-21T17:32:28Z"
                },
                {
                    "id": 11,
                    "chatTitle": "Issue with login credentials",
                    "timestamp": "2017-07-21T17:33:28Z"
                },
                {
                    "id": 12,
                    "chatTitle": "Account verification process",
                    "timestamp": "2017-07-21T17:34:28Z"
                },
                {
                    "id": 13,
                    "chatTitle": "Password reset request",
                    "timestamp": "2017-07-21T17:35:28Z"
                },
                {
                    "id": 14,
                    "chatTitle": "Billing inquiry for July",
                    "timestamp": "2017-07-21T17:36:28Z"
                },
                {
                    "id": 15,
                    "chatTitle": "Problem accessing dashboard",
                    "timestamp": "2017-07-21T17:37:28Z"
                },
                {
                    "id": 16,
                    "chatTitle": "Feature request: Dark mode",
                    "timestamp": "2017-07-21T17:38:28Z"
                },
                {
                    "id": 17,
                    "chatTitle": "Unable to upload files",
                    "timestamp": "2017-07-21T17:39:28Z"
                },
                {
                    "id": 18,
                    "chatTitle": "API integration issues",
                    "timestamp": "2017-07-21T17:40:28Z"
                },
                {
                    "id": 19,
                    "chatTitle": "Query about data export",
                    "timestamp": "2017-07-21T17:41:28Z"
                },
            ]
        }
    }

    if offset == 0:
        chat_list["data"]["next"] = "/users/?offset=10&limit=10"
    elif offset == 10:
        chat_list["data"]["previous"] = "/users/?offset=0&limit=10"
    else:
        return HTTPException(status_code=404)

    return JSONResponse(status_code=200, content=chat_list)


@chat_router.get("/chat/{chat_id}")
async def get_chat_history(chat_id: str):
    if chat_id == "00b8d29e-8cd3-4f11-88c7-5bda429d1560":
        chat_history = {
            "message": "Successfully fetched the chat history",
            "data": {
                "id": "00b8d29e-8cd3-4f11-88c7-5bda429d1560",
                "chatTitle": "About SFM",
                "timestamp": "2017-07-21T17:32:28Z",
                "messages": [
                    {
                        "role": "human",
                        "content": "What is SFM?",
                        "timestamp": "2017-07-21T17:32:28Z"
                    },
                    {
                        "role": "assistant",
                        "content": " {\"type\": \"static\", \"category\": \"SFM\", \"content\": \"SFM stands for System, Network, and Facility Management. It is a discipline that focuses on the management of IT infrastructure, including hardware, software, networks, and facilities, to ensure the smooth operation of an organization's IT systems.\"}<|end|>",
                        "timestamp": "2017-07-21T17:32:28Z",
                        "confidence": 70.3,
                    },
                    {
                        "role": "human",
                        "content": "I want to know my current salary",
                        "timestamp": "2017-07-21T17:32:28Z"
                    },
                    {
                        "role": "assistant",
                        "content": " {\"type\": \"dynamic\", \"category\": \"HR\", \"content\": \"dynamic_content\"}<|end|>",
                        "timestamp": "2017-07-21T17:32:28Z",
                        "confidence": 80.3,
                    },
                    {
                        "role": "tool",
                        "content": "my_current_salary",
                        "timestamp": "2017-07-21T17:32:28Z",
                    },
                    {
                        "role": "tool_response",
                        "content": "10000",
                        "timestamp": "2017-07-21T17:32:28Z",
                    },
                    {
                        "role": "human",
                        "content": "Say about an activity performed by the LnD team",
                        "timestamp": "2017-07-21T17:32:28Z"
                    },
                    {
                        "role": "assistant",
                        "content": " {\"type\": \"static\", \"category\": \"LnD\", \"content\": \"The primary aim of the Marketing Team at Experion is to promote the vision, brand, and business of Experion by developing and implementing strategies that result in new business opportunities for the company.\"}<|end|>",
                        "timestamp": "2017-07-21T17:32:28Z",
                        "confidence": 30.3,
                    },
                ]
            }
        }
    else:
        return HTTPException(status_code=404)

    return JSONResponse(status_code=200, content=chat_history)


@chat_router.delete("/chat/{chat_id}")
async def remove_chat_history():
    pass


@chat_router.post("/chat")
async def create_chat(chat_request: ChatRequestModel):
    sfm_static_dummy_response = {
        "message": "Successfully created new chat message",
        "data": {
            "chatId": "00b8d29e-8cd3-4f11-88c7-5bda429d1560",
            "role": "assistant",
            "content": " {\"type\": \"static\", \"category\": \"SFM\", \"content\": \"SFM stands for System, Network, and Facility Management. It is a discipline that focuses on the management of IT infrastructure, including hardware, software, networks, and facilities, to ensure the smooth operation of an organization's IT systems.\"}<|end|>",
            "timestamp": "2017-07-21T17:32:28Z",
            "confidence": 70.3,
        },
    }

    hr_dynamic_dummy_response = {
        "message": "Successfully created new chat message",
        "data": {
            "chatId": "00b8d29e-8cd3-4f11-88c7-5bda429d1560",
            "role": "assistant",
            "content": " {\"type\": \"dynamic\", \"category\": \"HR\", \"content\": \"dynamic_content\"}<|end|>",
            "timestamp": "2017-07-21T17:32:28Z",
            "confidence": 80.3,
        },
    }

    lnd_static_dummy_response = {
        "message": "Successfully created new chat message",
        "data": {
            "chatId": "00b8d29e-8cd3-4f11-88c7-5bda429d1560",
            "role": "assistant",
            "content": " {\"type\": \"static\", \"category\": \"LnD\", \"content\": \"The primary aim of the Marketing Team at Experion is to promote the vision, brand, and business of Experion by developing and implementing strategies that result in new business opportunities for the company.\"}<|end|>",
            "timestamp": "2017-07-21T17:32:28Z",
            "confidence": 30.3,
        },
    }

    default_dummy_response = {
        "message": "Successfully created new chat message",
        "data": {
            "chatId": "00b8d29e-8cd3-4f11-88c7-5bda429d1560",
            "role": "assistant",
            "content": " {\"type\": \"static\", \"category\": \"Default\", \"content\": \"I cannot answer your question based on our data source. Please try again with a different query!!!\"}<|end|>",
            "timestamp": "2017-07-21T17:32:28Z",
            "confidence": 70.3,
        },
    }

    tool_dummy_response = {
        "message": "Successfully created new chat message",
        "data": {},
    }

    if chat_request.data[0].role == "tool" or chat_request.data[0].role == "tool_response":
        return JSONResponse(status_code=201, content=tool_dummy_response)
    elif chat_request.data[0].role == "human":
        content = chat_request.data[0].content
        if "sfm" in content.lower():
            return JSONResponse(status_code=201, content=sfm_static_dummy_response)
        elif "hr" in content.lower():
            return JSONResponse(status_code=201, content=hr_dynamic_dummy_response)
        elif "lnd" in content.lower():
            return JSONResponse(status_code=201, content=lnd_static_dummy_response)
        else:
            return JSONResponse(status_code=201, content=default_dummy_response)
    else:
        return HTTPException(status_code=400)


# @chat_router.post("/chat")
# async def create_chat(
#     chat_request: ChatRequestModel,
#     x_user_token: str = Header(None),
#     ai_client: AIClient = Depends(OpenAIClient),
# ):

#     messages = []
#     user = None

#     if x_user_token:
#         # Fetch the user
#         pass

#     chat_id = chat_request.chatId
#     if chat_id:
#         # TODO Logic for saving tools and tools response
#         # 1. Check if the data contains tools and tools_response
#         # 2. Fetch the history
#         # 3. Save the tools and tools_response in it
#         # Fetch the history corresponding to that chat id
#         pass

#     messages.append(chat_request.data)

#     messages = ai_client.chat_message_formatter(messages=messages)

#     chat_response = await ChatService.infer_from_text(
#         messages=messages, ai_client=ai_client
#     )
#     chat_response.chatId = chat_id
#     saved_chat = await ChatHistoryService.save_chat_to_history(user, chat_response)

#     response = ResponseModel(message="Success", data=saved_chat)
#     return JSONResponse(status_code=201, content=response.model_dump())
