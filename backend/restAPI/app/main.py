from os import getenv, path
from dotenv import load_dotenv, find_dotenv

from typing import Union
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.routers import add_data, search, charts, vars

load_dotenv(find_dotenv())

app = FastAPI()
api_app = FastAPI()

origins = [
    "*",
    "http://localhost:80",
    "http://localhost",
    f"https://localhost:{getenv('REST_API_OUTER_APP_PORT', 5000)}",
    f"https://localhost:{getenv('REST_API_APP_PORT', 5000)}",
    f"http://localhost:{getenv('REST_API_OUTER_APP_PORT', 5000)}",
    f"http://localhost:{getenv('REST_API_APP_PORT', 5000)}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO, filename="restAPI.log", format="%(asctime)s %(levelname)s %(message)s")

api_app.include_router(add_data.router)
api_app.include_router(search.router)
api_app.include_router(charts.router)
api_app.include_router(vars.router)

logging.info('Routes loaded.')



@api_app.get("/")
def read_root():
    return {"Hello": "World"}

@api_app.get("/ping")
def read_root():
    return "pong"

app.mount("/api", api_app)
