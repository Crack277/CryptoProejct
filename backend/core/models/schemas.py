from pydantic import BaseModel, ConfigDict


class CryptoBase(BaseModel):
    name: str
    price: float
    percent_change_24h: float
    market_cap: float

class Crypto(CryptoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int