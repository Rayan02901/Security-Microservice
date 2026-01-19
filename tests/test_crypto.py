from app.services.encryption_service import encrypt_data, decrypt_data
import time
import pytest

def test_encrypt_decrypt():
    token = encrypt_data("secret")
    result = decrypt_data(token)
    assert result == "secret"

def test_token_expiry():
    token = encrypt_data("expired")
    time.sleep(2)
    with pytest.raises(ValueError):
        decrypt_data(token, ttl=1)

