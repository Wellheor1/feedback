from fastapi import FastAPI, Body, Query

from crud import add_review, search_review
from models import Reviews
from schemas import ReviewBodyParam, ReviewsQueryParam

app = FastAPI()


@app.post("/reviews", summary="Создание отзыва")
async def create_reviews(request_body: ReviewBodyParam = Body()):
    review = request_body.text
    review_lower = review.lower()
    sentiments = {"хорош": "positive", "люблю": "positive", "плохо": "negative", "ненавиж": "negative"}
    sentiment = "neutral"
    for key, value in sentiments.items():
        if key in review_lower:
            sentiment = value
    result = await add_review(review, sentiment)
    return {"id": result.id, "text": result.text, "sentiment": result.sentiment, "created_at": result.created_at}


@app.get("/", summary="Получение отзывов по параметрам")
async def get_reviews(query_params: ReviewsQueryParam = Query()):
    sentiment = query_params.sentiment
    result = await search_review(sentiment)
    return result
