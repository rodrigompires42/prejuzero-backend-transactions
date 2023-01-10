import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

from fastapi import FastAPI

dotenv_path = join(dirname(dirname(__file__)), ".env")
load_dotenv(dotenv_path)

USERS_MICROSERVICE_PORT = os.environ.get("USERS_MICROSERVICE_PORT")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "transactions microservice"}


@app.get("/transactions/{user_id}")
def list_transactions_by_user(user_id: int):
    response = requests.get(f"http://localhost:{USERS_MICROSERVICE_PORT}/users/{user_id}")
    user = response.json()
    return {"user": user["user_name"], "transactions": [{"teste"}]}