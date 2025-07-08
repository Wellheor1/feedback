from datetime import datetime

from database import async_session_maker
from models import Reviews
from sqlalchemy import select, text


async def add_review(text_reviews: str, sentiment: str):
    async with async_session_maker() as session:
        review = Reviews(text=text_reviews, sentiment=sentiment, created_at=datetime.utcnow().isoformat())
        session.add(review)
        await session.commit()
        await session.refresh(review)
        return review


### Если обязательно sql, то sqlite так себе вариант (нет RETURNING)
### Если их использовать необходимо в api учесть что возвращатся dict
async def add_review_sql(text_reviews: str, sentiment: str):
    created_at = datetime.utcnow().isoformat()
    async with async_session_maker() as session:
        await session.execute(
            text("""
                INSERT INTO reviews (text, sentiment, created_at)
                VALUES (:text, :sentiment, :created_at)
            """),
            {"text": text_reviews, "sentiment": sentiment, "created_at": created_at}
        )
        result = await session.execute(text("SELECT last_insert_rowid()"))
        last_id = result.scalar()

        result = await session.execute(
            text("""
                        SELECT id, text, sentiment, created_at
                        FROM reviews
                        WHERE id = :id
                    """),
            {"id": last_id}
        )
        row = result.fetchone()
        return dict(row._mapping) if row else None


async def search_review(sentiment: str):
    async with async_session_maker() as session:
        query = select(Reviews).where(Reviews.sentiment == sentiment)
        result = await session.execute(query)
        return result.scalars().all()


async def search_review_sql(sentiment: str):
    async with async_session_maker() as session:
        result = await session.execute(
            text("""
                SELECT id, text, sentiment, created_at
                FROM reviews
                WHERE sentiment = :sentiment
            """),
            {"sentiment": sentiment}
        )
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]
