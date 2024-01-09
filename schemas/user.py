from pydantic import BaseModel, Field



class User(BaseModel):

    username: str = Field(default='Undefiend', max_length=10, min_length=3)
    age: int = Field(ge=18, le=99)
