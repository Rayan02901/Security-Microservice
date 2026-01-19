from fastapi import FastAPI
from app.api import health, crypto, logs
from app.core.logging import get_logger

logger = get_logger()

app = FastAPI(
    title="Security Microservice",
    description="Encryption & Security Learning Microservice",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(crypto.router)
app.include_router(logs.router)

@app.on_event("startup")
def startup():
    logger.info("Service started")
