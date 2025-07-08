import datetime

from database import async_session_maker
from models import Reviews


async def create(text: str, sentiment: str):
    async with async_session_maker() as session:
        review = Reviews(text=text, sentiment=sentiment, created_at=datetime.utcnow().isoformat())
        session.add(review)
        await session.commit()
        await session.refresh(review)
        return review
