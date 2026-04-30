from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data):
    to_encode = data.copy()

    expire = datetime.timezone('Asia/Kolkata') + timedelta(hours=2)

    to_encode.update({
        "exp": expire
    })#add expiry into payload, so that token becomes invalid after 2 hours

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )#converts payload to token

    return token #send token back to user after successful login, which can be used for authentication in future requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#token will come from Authorization header in the format "Bearer <token>"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        user_id = payload.get("user_id")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return {
            "username": username,
            "user_id": user_id
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token is invalid or expired"
        )