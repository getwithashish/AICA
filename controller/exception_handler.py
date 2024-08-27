from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from exceptions import (
    ChatSessionNotFoundException,
    InvalidDataException,
    UnauthorizedUserException,
)
from messages import CHAT_SESSION_NOT_FOUND, METHOD_NOT_ALLOWED, VALIDATION_FAILED
from model.response_model import ResponseModel


async def invalid_data_exception_handler(request: Request, exc: InvalidDataException):
    response = ResponseModel(message=exc.message, data={})
    return JSONResponse(status_code=400, content=response.model_dump())


async def unauthorized_user_exception_handler(
    request: Request, exc: UnauthorizedUserException
):
    response = ResponseModel(message=exc.message, data={})
    return JSONResponse(status_code=401, content=response.model_dump())


async def chat_session_not_found_exception_handler(
    request: Request, exc: UnauthorizedUserException
):
    message = CHAT_SESSION_NOT_FOUND.format(chat_id=exc.chat_id)
    response = ResponseModel(message=message, data={})
    return JSONResponse(status_code=404, content=response.model_dump())


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    response = ResponseModel(message=VALIDATION_FAILED, data={})
    return JSONResponse(status_code=422, content=response.model_dump())


async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 405:
        response = ResponseModel(message=METHOD_NOT_ALLOWED, data={})
        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(),
        )
    else:
        response = ResponseModel(message=METHOD_NOT_ALLOWED, data={})
        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(),
        )


def include_exception_handler_in_app(app: FastAPI):
    app.add_exception_handler(InvalidDataException, invalid_data_exception_handler)
    app.add_exception_handler(
        UnauthorizedUserException, unauthorized_user_exception_handler
    )
    app.add_exception_handler(
        ChatSessionNotFoundException, chat_session_not_found_exception_handler
    )
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
