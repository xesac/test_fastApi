from fastapi.responses import JSONResponse
from fastapi import status
from schemas.user import find_person

def find_user(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            status_code = status.HTTP_404_NOT_FOUND,
            content = {'message': 'Пользователь не найден'}
        )
    return person