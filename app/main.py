from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = (
    Path(__file__).resolve().parent
)  # 현재파일의 경로 + Parent(현재파일의 부모폴더)

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "title": "Collector"}
    return templates.TemplateResponse(name="./index.html", context=context)


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    context = {"request": request, "title": "Collector", "keyword": q}
    return templates.TemplateResponse(name="./index.html", context=context)
