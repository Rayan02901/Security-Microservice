from loguru import logger
from pathlib import Path
from app.core.config import LOG_LEVEL

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.add(
    LOG_DIR / "app.log",
    rotation="1 day",
    retention="2 days",
    level=LOG_LEVEL,
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger
