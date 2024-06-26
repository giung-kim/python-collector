from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.book import BookModel
from app.book_scraper import NaverBookScraper


BASE_DIR = (
    Path(__file__).resolve().parent
)  # 현재파일의 경로 + Parent(현재파일의 부모폴더)

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(
    #     keyword="파이썬", publisher="BJPublic", price=1200, image="me.png"
    # )  # Test
    # await mongodb.engine.save(book)  # DB에 저장
    context = {"request": request, "title": "Collector"}
    return templates.TemplateResponse(name="./index.html", context=context)


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):

    # 1. 쿼리에서 검색어  추출
    # #(예외처리)
    # 검색어가 없다면 사용자에게 검색을 요구
    # 해당 검색어에대해 수집된 데이터가 DB에 존재한다면 사용자에게 보여줌 return
    # 2. 데이터수집기로 해당 검색어에대해 수집
    # 3. DB에 수집된 데이터를 저장
    # 수집된 각각의 데이터에 대해서 DB에 들어갈 모델 인스턴스 찍음
    # 각 모델 인스턴스르f DB에 저장

    # 1
    keyword = q

    # 2
    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10)
    book_models = []

    for book in books:
        # 디버깅 메시지 추가
        print(f"Book data: {book}")

        # "discount" 키가 있는지 확인
        if "discount" not in book:
            raise HTTPException(
                status_code=404, detail="Discount not found in book data"
            )

        try:
            # discount 값 확인
            discount_value = book["discount"]
            print(f"Discount value before conversion: {discount_value}")

            # discount 값을 정수로 변환
            price_value = int(discount_value)
            print(f"Price value after conversion: {price_value}")

            book_model = BookModel(
                keyword=keyword,
                publisher=book["publisher"],
                price=price_value,  # discount 값을 price로 사용하고 정수로 변환
                image=book["image"],
            )
            book_models.append(book_model)
        except Exception as e:
            print(f"Error creating book model: {e}")
            raise HTTPException(status_code=500, detail="Error creating book model")

    # 3
    await mongodb.engine.save_all(book_models)

    context = {
        "request": request,
        "title": "Collector",
        "keyword": q,
        "books": book_models,
    }
    return templates.TemplateResponse(name="./index.html", context=context)


@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()
    print("DB Connected")


@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    mongodb.close()
