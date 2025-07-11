from contextlib import asynccontextmanager

from fastapi import FastAPI, Body, Query

from app.crud import add_review, search_review
from app.database import init_db
from app.schemas import ReviewBodyParam, ReviewsQueryParam
from app.utils import create_sentiment


@asynccontextmanager
async def lifespan(application: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/reviews", summary="Создание отзыва")
async def create_reviews(request_body: ReviewBodyParam = Body()):
    review = request_body.text
    sentiment = create_sentiment(review)
    result = await add_review(review, sentiment)
    return {"id": result.id, "text": result.text, "sentiment": result.sentiment, "created_at": result.created_at}


@app.get("/", summary="Получение отзывов по параметру")
async def get_reviews(query_params: ReviewsQueryParam = Query()):
    sentiment = query_params.sentiment
    result = await search_review(sentiment)
    return result
