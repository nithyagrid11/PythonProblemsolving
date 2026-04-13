from fastapi import FastAPI, Response
from analyzer import analyze_logs_from_lines
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from database import connect_db
import json

logs_history = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], #allows all domains to access this API
    allow_credentials=True, #allows cookies and authentication headers
    allow_methods = ["*"], #allows all HTTP methods
    allow_headers=["*"], #allows all headers in requests
)

class LogInput(BaseModel):
    content: str
# here {"content": "logs..."} got from JS and Fastapi converts to processed output that is the object


@app.get("/")
def home():
    return {"message": "Smart Log Analyzer API is running"} #message for home page
@app.get("/favicon.ico")
def favicon():
    return Response(status_code = 204) #204 - no content, browser stays quiet
@app.post("/analyze")
def run_analysis(data: LogInput):
    log_lines = data.content.split("\n") #converts string to list of lines
    result = analyze_logs_from_lines(log_lines)
    '''logs_history.append({
        "logs": data.content,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return result #fastapi converts python->json automatically'''
    total = result["total_count"]
    errors = result["total_errors"]
    warnings = result["total_warnings"]

    result_json = json.dumps(result)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO log_history (logs, total_count, error_count, warning_count, result_json) VALUES (%s, %s, %s, %s, %s)", (data.content, total, errors, warnings, result_json))
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

@app.get("/history")
def get_history():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * from log_history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return {"history":rows}