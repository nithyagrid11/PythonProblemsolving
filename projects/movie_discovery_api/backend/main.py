from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
async def get_all():
    return movies_db

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