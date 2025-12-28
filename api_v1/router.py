from fastapi import APIRouter

from core.config import settings
from .init import cmc_client

router = APIRouter(prefix=settings.api_key.prefix)


@router.get("/")
async def get_list_of_currency():
    return await cmc_client.get_list_of_currency()


@router.get("/{currency_id}/")
async def get_currency_from_id(currency_id: int):
    return await cmc_client.get_currency_from_id(currency_id=currency_id)