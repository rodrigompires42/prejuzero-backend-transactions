import os
from os.path import join, dirname
from dotenv import load_dotenv

from fastapi import FastAPI

dotenv_path = join(dirname(dirname(__file__)), ".env")
load_dotenv(dotenv_path)

USERS_MICROSERVICE_PORT = os.environ.get("USERS_MICROSERVICE_PORT")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "transactions microservice"}


@app.get("/transactions")
def list_transactions():
    return {"transactions": "teste"}