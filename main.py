from fastapi import FastAPI, Form, status
from schemas.user import User
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse


app = FastAPI(title='REST API TEST')


@app.get("/")
def root():
    users = [User('fuck', 10) for i in range(100)]
    return HTMLResponse(f'<h1>{users}</h1>')
