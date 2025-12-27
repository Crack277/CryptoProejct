from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from core.models import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    return {"message": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)