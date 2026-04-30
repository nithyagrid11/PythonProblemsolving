from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.log_routes import router
from api.auth_routes import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Smart Log Analyzer API is running"}