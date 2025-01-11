from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

users_db = [
    User(id=1, username="user1", email="user1@example.com"),
    User(id=2, username="user2", email="user2@example.com"),
    User(id=3, username="user3", email="user3@example.com")
]

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/users")
def get_all_users():
    return users_db

@app.post("/create_user", response_model=User)
def create_user(new_user: User):
    for user in users_db:
        if user.id == new_user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(new_user)
    