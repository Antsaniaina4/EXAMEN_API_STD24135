from fastapi import FastAPI, Request, Query
from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()
@app.get('/ping')
def ping():
    return "Pong", res.status_code(200)

