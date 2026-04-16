from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database import cursor
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

movies_db = []
class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
    is_available: bool
    genre: str
    rating: int

@app.post("/addmovie")
def add_movie(addmovie: Movie):
    movies_db.append(addmovie.model_dump())
    return {"status": "added"}

@app.get("/getall")
async def get_all(page: int = 1, limit: int =5, name: str = None, genre: str = None, rating: int = None):
    query = "select * from movies where 1=1"
    values = []
    
    if name:
        query += " AND title ILIKE %s"
        values.append(f"%{name}%")
    if genre:
        query += " AND genre ILIKE %s"
        values.append(genre)
    if rating:
        query += " AND rating >= %s"
        values.append(rating)
    
    offset = (page-1) * limit
    query += " LIMIT %s OFFSET %s"
    values.extend([limit,offset])

    cursor.execute(query,values)
    rows = cursor.fetchall()

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

@app.get("/featured")
def get_featured():
    cursor.execute("SELECT * FROM movies WHERE is_featured = TRUE")
    rows = cursor.fetchall()

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

@app.delete("/movie/{movie_id}")
def delete_movie(movie_id: int):
    global movies_db
    movies_db = [m for m in movies_db if m["id"] != movie_id]
    return {"message": "deleted"}

@app.put("/movie/{movieid}")
def update_movie(movieid: int, updated_movie: Movie):
    global movies_db
    for i, movie in enumerate(movies_db):
        if movieid == movie["id"]:
            movies_db[i] = updated_movie.model_dump()
            return {"message": "success"}
    return{"message": "not found"}
#testing
#testing