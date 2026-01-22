from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from core.router import router as router_v1


app = FastAPI()
app.include_router(router=router_v1)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)