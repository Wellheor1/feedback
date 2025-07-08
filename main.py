from fastapi import FastAPI, Body, Query

from crud import add_review, search_review, add_review_sql, search_review_sql
from schemas import ReviewBodyParam, ReviewsQueryParam
from utils import create_sentiment

app = FastAPI()


@app.post("/reviews", summary="Создание отзыва")
async def create_reviews(request_body: ReviewBodyParam = Body()):
    review = request_body.text
    sentiment = create_sentiment(review)
    result = await add_review(review, sentiment)
    return {"id": result.id, "text": result.text, "sentiment": result.sentiment, "created_at": result.created_at}


@app.get("/", summary="Получение отзывов по параметрам")
async def get_reviews(query_params: ReviewsQueryParam = Query()):
    sentiment = query_params.sentiment
    # result = await search_review(sentiment)
    result = await search_review_sql(sentiment)
    return result
