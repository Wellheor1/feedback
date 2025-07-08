from sqlalchemy import Column, Integer, String
from app.database import Base


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    sentiment = Column(String, index=True)
    created_at = Column(String)
