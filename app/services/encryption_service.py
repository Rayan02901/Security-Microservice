from datetime import datetime, timezone
from cryptography.fernet import InvalidToken
from app.services.key_service import get_fernet
from app.core.config import TOKEN_TTL_SECONDS

def encrypt_data(plain_text: str) -> str:
    fernet = get_fernet()
    token = fernet.encrypt(plain_text.encode())
    return token.decode()

def decrypt_data(token: str, ttl: int | None = None) -> str:
    fernet = get_fernet()
    try:
        decrypted = fernet.decrypt(
            token.encode(),
            ttl=ttl
        )
        return decrypted.decode()
    except InvalidToken:
        raise ValueError("Token expired or invalid")
