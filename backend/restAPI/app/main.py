from os import getenv, path
from dotenv import load_dotenv, find_dotenv

from typing import Union

from fastapi import FastAPI
from modules.routers import add_data, search

load_dotenv(find_dotenv())

app = FastAPI()
app.include_router(add_data.router)
app.include_router(search.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping")
def read_root():
    return "pong"

