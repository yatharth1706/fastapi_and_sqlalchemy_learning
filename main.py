from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from path_parameters import path
from enum_parameters import enumParam
from query_parameters import query_params
from body import body
from body_with_parameters import with_params

app = FastAPI()
app.include_router(path.router)
app.include_router(enumParam.router)
app.include_router(query_params.router)
app.include_router(body.router)
app.include_router(with_params.router, prefix="/api")

@app.get("/")
def test_api():
    return {"message": "Hello world"}