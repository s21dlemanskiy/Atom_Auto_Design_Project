from os import getenv, path
from dotenv import load_dotenv, find_dotenv

from typing import Union
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.routers import add_data, search, charts

load_dotenv(find_dotenv())

app = FastAPI()

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

logging.basicConfig(level=logging.INFO, filename="/var/log/restAPI.log", format="%(asctime)s %(levelname)s %(message)s")

app.include_router(add_data.router)
app.include_router(search.router)
app.include_router(charts.router)

logging.info('Routes loaded.')



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping")
def read_root():
    return "pong"

