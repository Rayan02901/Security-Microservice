from cryptography.fernet import Fernet
from app.core.config import FERNET_KEY

_fernet = Fernet(FERNET_KEY.encode())

def get_fernet() -> Fernet:
    return _fernet
