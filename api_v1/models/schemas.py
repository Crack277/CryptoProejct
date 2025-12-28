from pydantic import BaseModel, ConfigDict


class CryptoBase(BaseModel):
    name: str
    symbol: str
    price: float
    last_updated: str

class Crypto(CryptoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int