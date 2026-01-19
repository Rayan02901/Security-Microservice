from pydantic import BaseModel

class EncryptRequest(BaseModel):
    data: str

class EncryptResponse(BaseModel):
    token: str

class DecryptRequest(BaseModel):
    token: str

class DecryptResponse(BaseModel):
    data: str
