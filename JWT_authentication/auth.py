#JWT- creation and verfication token
from authlib.jose import JoseError,jwt
from fastapi import FastAPI, HTTPException
from datetime import datetime,timedelta,timezone


SECRET_KEY='my_secret'
ALOGRITHM='HS246'
ACCESS_TOKEN_EXIPERY_MINUTES=30

def create_access_token(data:dict):
    header={'alg':ALOGRITHM}
    expire=datetime.now(timezone.utc)+ timedelta(ACCESS_TOKEN_EXIPERY_MINUTES)
    payload=data.copy()
    payload.update({'exp':expire})
    return jwt.encode(header,payload,SECRET_KEY).decode('utf-8')


def verify_token(token:str):
    try:
        claims=jwt.decode(token,SECRET_KEY)
        claims.validate()
        username=claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401,detail='Token missing')
        return username
    except JoseError:
        raise HTTPException(status_code=401, detail='invalid cred')
    