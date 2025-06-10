from fastapi import APIRouter, status, Path, Query, Body
from typing import Annotated

from .manual_schema import (
    GetManualsResponse,
    GetManualResponse,
    GetSearchManualsReponse,
    PostManualResponse,
    PostManualInput,
)

router = APIRouter(
    prefix="/manual",
    tags=["Manual"],
)


@router.get("", response_model=GetManualsResponse, status_code=status.HTTP_200_OK)
async def get_manuals(): ...


@router.get("/", response_model=GetSearchManualsReponse, status_code=status.HTTP_200_OK)
async def search_manual(query: Annotated[str, Query()]): ...


@router.get(
    "/{manual_id}", response_model=GetManualResponse, status_code=status.HTTP_200_OK
)
async def get_manual(manual_id: Annotated[str, Path()]): ...


@router.post("", response_model=PostManualResponse, status_code=status.HTTP_200_OK)
async def upload_manual(manual_upload: Annotated[PostManualInput, Body()]): ...
