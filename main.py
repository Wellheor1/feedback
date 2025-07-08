from fastapi import FastAPI, Body, Query
from schemas import ReviewBodyParam, ReviewsQueryParam

app = FastAPI()


@app.post("/reviews", summary="Создание отзыва")
async def create_reviews(request_body: ReviewBodyParam = Body()):
    review = request_body.text
    return {"id": 1, "text": review, "sentiment": "", "created_at": "2025-02-02"}


@app.get("/", summary="Получение отзывов по параметрам")
async def get_reviews(query_params: ReviewsQueryParam = Query()):
    sentiment = query_params.sentiment
    return {"ok": True, "message": "Hello World Well"}
