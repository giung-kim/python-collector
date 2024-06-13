from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("hello world!")
    return {"Hello": "World"}


@app.get("/hello")
def read_fastapi_hello():
    print("hello world!")
    return {"Hello": "FastAPI"}


@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz:str ,q: Union[str, None] = None):
    return {"item_id": item_id, "q": q,"xyz": xyz}