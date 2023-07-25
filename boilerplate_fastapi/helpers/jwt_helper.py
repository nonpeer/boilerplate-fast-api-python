import os
from decouple import config

import jwt


def encode(payload: dict) -> str:
    secret = config('SECRET', 'secret', cast=str)
    return jwt.encode(payload=payload, key=secret, algorithm="HS256")


def decode(token: str) -> dict:
    try:
        secret = config('SECRET', 'secret', cast=str)
        return jwt.decode(jwt=token, key=secret, algorithms=["HS256"])
    except Exception:
        return {}