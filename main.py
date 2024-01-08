from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
from pydantic import BaseModel



app = FastAPI()

class User(BaseModel):
    
    name: str
    age: int
    email: str
    password: str


@app.post('/create_user')
def create_user(user_model: User):
    return 'a'

