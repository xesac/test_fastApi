from schemas.user import User
from fastapi import status
from fastapi.responses import JSONResponse

persons = []

def add_user(user: User):
    if user not in persons:
        persons.append(user)
    else:
        return JSONResponse(status_code=status.HTTP_103_EARLY_HINTS, content={'message': 'Пользователь уже в базе'})
    
