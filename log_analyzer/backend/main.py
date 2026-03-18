from fastapi import FastAPI, Response
from analyzer import analyze_logs

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Log Analyzer API is running"} #message for home page
@app.get("/favicon.ico")
def favicon():
    return Response(status_code = 204) #204 - no content, browser stays quiet
@app.get("/analyze")
def run_analysis():
    result = analyze_logs("server.log")
    return result