from fastapi import FastAPI
from analyzer import analyze_logs

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Log Analyzer API is running"}
@app.get("/analyze")
def run_analysis():
    result = analyze_logs("server.log")
    return result