import datetime

from database import async_session_maker
from models import Reviews
from sqlalchemy import (select)


async def add_review(text: str, sentiment: str):
    async with async_session_maker() as session:
        review = Reviews(text=text, sentiment=sentiment, created_at=datetime.utcnow().isoformat())
        session.add(review)
        await session.commit()
        await session.refresh(review)
        return review


async def search_review(sentiment: str):
    async with async_session_maker() as session:
        query = select(Reviews).where(Reviews.sentiment == sentiment)
        result = await session.execute(query)
        return result.scalars().all()