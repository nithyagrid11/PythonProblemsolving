from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
    is_available: bool
    genre: str
    rating: int

class FilterRequest(BaseModel):
    genre: str | None = None
    rating: float | None = None