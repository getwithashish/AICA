# AICA - AI Conversational Agent

## Overview
The AI Conversational Assistant is a powerful chatbot application designed to seamlessly interact with various AI models, providing users with dynamic and engaging conversations that feel almost human! 🤖✨ Built using FastAPI, this application leverages the asynchronous capabilities of Python to deliver real-time responses faster than you can say "ChatGPT!"

With Beanie for MongoDB integration, the application ensures efficient data handling and persistence, making it easy to store chat history. 🗄️💬 Plus, it calculates a confidence score in percentage, so you’ll know just how sure your virtual assistant is about its responses—no more guessing games! 🎯

Following the SOLID principles, the app is structured for maintainability, scalability, and robustness. Inversion of Control is implemented to enhance modularity and testability, allowing developers to easily swap out components like they’re changing outfits for a night out! 👗👔

# Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Run using Docker Compose](#run-using-docker-compose)
- [Setup for Development](#setup-for-development)
  - [Install Dependencies](#install-dependencies)
  - [Run Development Server](#run-development-server)
- [API Endpoints](#api-endpoints)
  - [Request and Response Models](#request-and-response-models)
    - [ChatRequestModel](#chatrequestmodel)
    - [ResponseModel](#responsemodel)
  - [Example Requests](#example-requests)
    - [Create Chat](#create-chat)
    - [List Chats](#list-chats)
  - [Example Responses](#example-responses)
    - [Create Chat Response](#create-chat-response)
    - [List Chats Response](#list-chats-response)
- [Contribution](#contribution)

## Project Structure
```
.
├── Dockerfile
├── README.md
├── client
│   ├── ai_client.py
│   ├── mongo
│   │   ├── config.py
│   │   └── mongo_client.py
│   └── openai
│       ├── config.py
│       └── openai_client.py
├── controller
│   ├── chat_controller.py
│   └── exception_handler.py
├── docker-compose.yml
├── exceptions.py
├── main.py
├── messages.py
├── model
│   ├── chat_list_response_model.py
│   ├── chat_message_model.py
│   ├── chat_model.py
│   ├── chat_request_model.py
│   ├── chat_response_model.py
│   └── response_model.py
├── repository
│   ├── chat_repo.py
│   ├── mongo
│   │   ├── mongo_chat_repo.py
│   │   └── mongo_user_repo.py
│   └── user_repo.py
├── requirements.txt
├── service
│   ├── chat_history_service.py
│   └── chat_service.py
└── util
    ├── chat_message_formatter.py
    ├── missing_dict_keys_finder.py
    └── string_to_uuid_converter.py
```

## Prerequisites

- Python 3.10+
- MongoDB
- Docker and Docker Compose (Optional)

> Note: **Add .env in with the configurations required for running the application**

```env
OPENAI_API_BASE=https://api.openai.com/v1/
OPENAI_KEY=api_key_here
MODEL_NAME=gpt-4o

USER_ROLE_NAME=user
ASSISTANT_ROLE_NAME=assistant
TITLE_PROMPT=Generate a 2-5 word title for this chat

DATABASE_URL=mongodb://chatbot:chatbot@mongodb-chatbot-db:27017
DATABASE_NAME=chat_db

```

## Run using Docker Compose

```bash
docker compose up
```

## Setup for Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Development Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8888
```

The development server will be hosted on http://localhost:8888 by default.

## API Endpoints

| Method | Endpoint           | Description                         | Request Body                     | Response                                      | Headers              |
|--------|--------------------|-------------------------------------|----------------------------------|-----------------------------------------------|----------------------|
| POST   | `/chat`            | Initiates a chat session           | `ChatRequestModel` (JSON)       | `ResponseModel` with chat response details    | `x-user-token: str`  |
| GET    | `/chat/list`       | Retrieves a list of user chats     | None                             | `ResponseModel` with list of chats            | `x-user-token: str`  |

x-user-token: Use a base64 encoded string to identify a user.

### Request and Response Models

#### ChatRequestModel
- **chatId**: `string` (optional) - The ID of the chat session.
- **data**: `array` (required) - An array of messages to initiate the chat.

#### ResponseModel
- **message**: `string` - A success or error message.
- **data**: `any` - The data returned by the API (e.g., chat response or chat list).

### Example Requests

#### Create Chat
```http
POST http://localhost:8888/v1/chat
Content-Type: application/json
x-user-token: Z2V0d2l0aGFzaGlzaEBnbWFpbC5jb20=

{
  "chatId": "example_chat_id",
  "data": [
    { "role": "user", "content": "Hello!" }
  ]
}
```

#### List Chats
```http
GET http://localhost:8888/v1/chat/list
x-user-token: Z2V0d2l0aGFzaGlzaEBnbWFpbC5jb20=
```

### Example Responses

#### Create Chat Response
```json
{
  "message": "Chat Request successfully completed",
  "data": {
		"role": "assistant",
		"content": "",
		"timestamp": "2024-10-08 09:43:13.749496",
		"confidence": 94.96837162525209,
		"chatId": "7aeafeeb-0880-4ab7-a8b4-520faecf551c"
	}
}
```

#### List Chats Response
```json
{
  "message": "The chat list of the user has been successfully retrieved",
  "data": {
		"userId": "a628c671-9a86-5654-bc2c-9435cc5ccec3",
		"chats": [
			{
				"_id": "6704fd7c0c403a95c145aa91",
				"user_id": "a628c671-9a86-5654-bc2c-9435cc5ccec3",
				"chat_id": "7aeafeeb-0880-4ab7-a8b4-520faecf551c",
				"chat_title": "Uncertain Outcomes: Israel's Conflict",
				"updated_at": "2024-10-08T09:38:31.400000",
				"messages": [
					{
						"role": "human",
						"content": "Will Israel win the war?",
						"timestamp": "2024-10-08T09:38:02.440000",
						"confidence": null
					},
					{
						"role": "assistant",
						"content": "The outcome of any conflict, including those involving Israel, is uncertain and depends on a wide range of factors, including military strategy, international diplomacy, political decisions, and humanitarian considerations. It's important to stay informed through reliable news sources and expert analyses to understand the evolving situation. Additionally, peace and resolution efforts are always preferable to prolonged conflict.",
						"timestamp": "2024-10-08T09:38:04.516000",
						"confidence": 79.67220596527027
					},
					{
						"role": "human",
						"content": "Who is the president?",
						"timestamp": "2024-10-08T09:38:29.691000",
						"confidence": null
					},
					{
						"role": "assistant",
						"content": "As of my last update, the President of Israel is Isaac Herzog. He took office on July 7, 2021. However, please verify with up-to-date sources, as political positions can change.",
						"timestamp": "2024-10-08T09:38:31.400000",
						"confidence": 96.35981994872775
					}
				]
			}
		]
	}
}
```

# Contribution

Feel free to open issues or pull requests if you find any bugs or have improvements.
