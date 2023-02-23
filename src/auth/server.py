import uvicorn
import jwt, datetime, os
from fastapi import FastAPI, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# uvicorn server:app --reload


@app.post('/login')
def login(form_data: schemas.UserLogin, db: SessionLocal = Depends(get_db)):
    res = crud.get_user_by_email(db, form_data.email)
    if res:
        email = res.email
        password = res.password
        if form_data.email != email or form_data.password != password:
            return "用户不存在", 401
        else:
            return create_jwt(form_data.email, os.getenv("JWT_SECRET", "token"), True)
    return "用户不存在", 401


@app.post("/validate")
def validate(request: Request):
    try:
        encoded_jwt = request.headers["Authorization"]
    except:
        return "令牌失效", 401
    encoded_jwt = encoded_jwt.split(" ")[1]
    try:
        decoded = jwt.decode(
            encoded_jwt, os.getenv("JWT_SECRET", "token"), algorithms=["HS256"]
        )
    except:
        return "令牌失效", 401

    return decoded


def create_jwt(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz
        },
        secret,
        algorithm="HS256"
    )