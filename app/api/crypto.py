from fastapi import APIRouter, HTTPException
from app.models.dto import (
    EncryptRequest, EncryptResponse,
    DecryptRequest, DecryptResponse
)
from app.services.encryption_service import encrypt_data, decrypt_data

router = APIRouter()

@router.post("/encrypt", response_model=EncryptResponse)
def encrypt(request: EncryptRequest):
    token = encrypt_data(request.data)
    return {"token": token}

@router.post("/decrypt", response_model=DecryptResponse)
def decrypt(request: DecryptRequest):
    try:
        data = decrypt_data(request.token)
        return {"data": data}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
