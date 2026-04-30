from fastapi import APIRouter, Response, Depends
from models.schemas import LogInput
from services.analyzer import analyze_logs_from_lines
from db.database import connect_db
from datetime import datetime
import json
from services.auth import get_current_user

router = APIRouter()

logs_history = []


@router.get("/favicon.ico")
def favicon():
    return Response(status_code=204)


@router.post("/analyze")
def run_analysis(data: LogInput, current_user: dict = Depends(get_current_user)):
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
        """
        INSERT INTO log_history
        (logs, total_count, error_count, warning_count, result_json, user_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
       (
          data.content,
          total,
          errors,
          warnings,
          result_json,
          current_user["user_id"]
       )
    )

    conn.commit()
    conn.close()

    return result


@router.get("/history")
def get_history(current_user: dict = Depends(get_current_user)):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
       """
       SELECT *
       FROM log_history
       WHERE user_id = %s
       ORDER BY id DESC
       """,
       (current_user["user_id"],)
    )

    rows = cursor.fetchall()

    conn.close()

    return {"history": rows}