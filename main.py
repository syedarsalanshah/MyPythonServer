from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Ali", "email": "ali@example.com"},
        {"id": 2, "name": "Sara", "email": "sara@example.com"}
    ]
    return users

@app.post("/users")
def create_user(user: User):
    return user

handler = Mangum(app)
