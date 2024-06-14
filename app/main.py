from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent    #현재파일의 경로 + Parent(현재파일의 부모폴더)

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR/"templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id,"data":"hello fast api"}
    )