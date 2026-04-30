# Smart Log Analyzer

A FastAPI + MySQL based project for analyzing server logs and detecting suspicious activities, errors, warnings, and traffic spikes.

---

## Features

- Log parsing using Regex
- Error detection (500–599 status codes)
- Warning detection (400–499 status codes)
- Suspicious IP detection based on repeated access
- Peak hour traffic detection
- Spike hour detection based on unusual usage
- HTTP method tracking (GET, POST, PUT, DELETE, etc.)
- Endpoint usage summary
- MySQL database storage for analysis history
- Frontend integration using HTML, CSS, and JavaScript

---

## Tech Stack

### Backend

- Python
- FastAPI
- MySQL
- Pydantic
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

---

## Project Structure

```text
log_analyzer/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── routes/
│   │   └── log_routes.py
│   │
│   ├── services/
│   │   └── analyzer.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── queries.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   └── sample_logs/
│       └── server.log
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── database/
│   └── setup.sql
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env