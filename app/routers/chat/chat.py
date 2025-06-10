from fastapi import APIRouter, status, Path, Query, Body
from typing import Annotated

from .chat_schema import (
    GetChatsResponse,
    GetSearchChatsReponse,
    GetChatResponse,
    PostChatResponse,
    PostChatInput,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.get("", response_model=GetChatsResponse, status_code=status.HTTP_200_OK)
async def get_chats(): ...


@router.get("/", response_model=GetSearchChatsReponse, status_code=status.HTTP_200_OK)
async def search_chat(query: Annotated[str, Query()]): ...


@router.get(
    "/{chat_id}", response_model=GetChatResponse, status_code=status.HTTP_200_OK
)
async def get_chat(chat_id: Annotated[str, Path()]): ...


@router.post("", response_model=PostChatResponse, status_code=status.HTTP_200_OK)
async def post_chat(chat_input: Annotated[PostChatInput, Body()]): ...
