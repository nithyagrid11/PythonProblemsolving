#This file handles User Registration + Login + Token Generation
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.schemas import UserRegister, UserLogin
from db.database import connect_db
from services.auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.post("/register")
def register(user: UserRegister):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (user.username,)
    )#checks if username already exists

    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_pw = hash_password(user.password)

    cursor.execute(
        """
        INSERT INTO users
        (username, email, password)
        VALUES (%s, %s, %s)
        """,
        (user.username, user.email, hashed_pw)
    )#inserting new user into database

    conn.commit()
    conn.close()

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (form_data.username,)
    )

    db_user = cursor.fetchone()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid username"
        )

    if not verify_password(form_data.password, db_user["password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid password"
        )

    token = create_access_token({
        "sub": form_data.username,
        "user_id": db_user["id"]
    })#creates token with username and user_id as payload, which can be used to identify the user in future requests

    conn.close()

    return {
        "access_token": token,
        "token_type": "bearer"
    }