from aiohttp import ClientSession
from .models.schemas import Crypto

class HttpClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                "X-CMC_PRO_API_KEY": api_key,
            }
        )

class CMCHttpClient(HttpClient):
    async def get_list_of_currency(self):
        async with self._session.get("/v1/cryptocurrency/listings/latest") as resp:
            result = await resp.json()
            return result["data"]

    async def get_currency_from_id(self, currency_id: int) -> Crypto:
        async with self._session.get("/v1/cryptocurrency/quotes/latest", params={"id": currency_id}) as resp:
            result = await resp.json()
            result = result["data"][str(currency_id)]
            crypto = ({
                "id": result["id"],
                "name": result["name"],
                "symbol": result["symbol"],
                "price": result["quote"]["USD"]["price"],
                "last_updated": result["quote"]["USD"]["last_updated"],
            })
            crypto_out = Crypto(**crypto)
            return crypto_out
