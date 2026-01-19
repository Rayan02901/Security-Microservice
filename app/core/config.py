import os
from dotenv import load_dotenv
from pathlib import Path

ENV = os.getenv("APP_ENV", "dev")

env_file = (
    ".env.prod" if ENV == "prod" else ".env.dev"
)

load_dotenv(dotenv_path=Path(env_file))

FERNET_KEY = os.getenv("FERNET_KEY")
TOKEN_TTL_SECONDS = int(os.getenv("TOKEN_TTL_SECONDS", "120"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

if not FERNET_KEY:
    raise RuntimeError("FERNET_KEY is not set")

if ENV == "prod":
    if len(FERNET_KEY) < 32:
        raise RuntimeError("Invalid FERNET_KEY length for production")
