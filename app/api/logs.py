from fastapi import APIRouter
from pathlib import Path

router = APIRouter()
LOG_FILE = Path("logs/app.log")

@router.get("/logs")
def get_logs():
    if not LOG_FILE.exists():
        return {"logs": []}
    return {"logs": LOG_FILE.read_text().splitlines()}
