from pydantic import BaseModel, Field


class ReviewBodyParam(BaseModel):
    text: str = Field(..., description="Ваш отзыв")


class ReviewsQueryParam(BaseModel):
    sentiment: str = Field(..., description="Тип отзыва")
