from fastapi import APIRouter, Depends
from app.models.movie import Movie
from app.db.queries import get_movies
from app.db.connection import get_db
from app.models.movie import FilterRequest
router = APIRouter()

@router.get("/getall") #search+filters+pagination
async def get_all(
    page: int = 1,
    limit: int = 5,
    name: str = None,
    genre: str = None,
    rating: float = None,
    db = Depends(get_db)
):
    query = "select * from movies where 1=1"
    values = []
    if name:
        query += " AND title ILIKE %s"
        values.append(f"%{name}%")
    if genre:
        query += " AND LOWER(genre) LIKE LOWER(%s)"
        values.append(f"%{genre.strip()}%")
    if rating is not None:
        query += " AND rating >= %s"
        values.append(float(rating))
    #pagination
    offset = (page - 1) * limit
    query += " LIMIT %s OFFSET %s"
    values.extend([limit, offset])
    rows = get_movies(db, query, values)#pass db

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "title": r[1],
            "genre": r[2],
            "rating": r[3],
            "year": r[4],
            "image_url": r[5],
            "description": r[6],
            "is_featured": r[7]
        })
    return result