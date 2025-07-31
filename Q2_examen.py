
from fastapi import FastAPI, Request, Query
from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()
@app.get('/home')
def home():
    return JSONResponse(content="<h1>Welcome home!</h1>", status_code=200)