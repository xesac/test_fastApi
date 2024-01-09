from fastapi import FastAPI, Path, Query, Body
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
 
class Person(BaseModel):
    name: str
    languages: list = []
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("public/index.html")
 
@app.post("/hello")
def hello(person: Person):
    return {"message": f"Name: {person.name}. Languages: {person.languages}"}