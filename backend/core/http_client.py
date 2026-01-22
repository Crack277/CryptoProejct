from aiohttp import ClientSession
from .models.schemas import Crypto

from async_lru import alru_cache

class HttpClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                "X-CMC_PRO_API_KEY": api_key,
            }
        )

class CMCHttpClient(HttpClient):

    @alru_cache()
    async def get_list_of_currency(self):
        async with self._session.get("/v1/cryptocurrency/listings/latest") as resp:
            result = await resp.json()
            return result["data"]

    @alru_cache()
    async def get_currency_from_id(self, currency_id: int) -> Crypto:
        async with self._session.get("/v1/cryptocurrency/quotes/latest", params={"id": currency_id}) as resp:
            result = await resp.json()
            result = result["data"][str(currency_id)]
            crypto = ({
                "id": result["id"],
                "name": result["name"],
                "price": result["quote"]["USD"]["price"],
                "percent_change_24h": result["quote"]["USD"]["percent_change_24h"],
                "market_cap": result["quote"]["USD"]["market_cap"],
            })
            crypto_out = Crypto(**crypto)
            return crypto_out
