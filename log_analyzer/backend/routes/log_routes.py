from fastapi import APIRouter, Response
from models.schemas import LogInput
from services.analyzer import analyze_logs_from_lines
from db.database import connect_db
from datetime import datetime
import json

router = APIRouter()

logs_history = []


@router.get("/favicon.ico")
def favicon():
    return Response(status_code=204)


@router.post("/analyze")
def run_analysis(data: LogInput):
    log_lines = data.content.split("\n")
    result = analyze_logs_from_lines(log_lines)

    '''
    logs_history.append({
        "logs": data.content,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return result
    '''

    total = result["total_count"]
    errors = result["total_errors"]
    warnings = result["total_warnings"]

    result_json = json.dumps(result)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO log_history (logs, total_count, error_count, warning_count, result_json) VALUES (%s, %s, %s, %s, %s)",
        (data.content, total, errors, warnings, result_json)
    )

    conn.commit()
    conn.close()

    return result


@router.get("/history")
def get_history():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * from log_history ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return {"history": rows}