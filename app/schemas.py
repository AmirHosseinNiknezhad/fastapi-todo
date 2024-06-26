from datetime import datetime
from typing import Union
from pydantic import BaseModel, EmailStr, conint


class TodoBase(BaseModel):
    title: str

    class Config:
        from_attributes = True


class TodoCreate(TodoBase):
    description: Union[str, None] = None
    importance: conint(ge=1, le=3) = 1


class Todo(TodoBase):
    id: int
    description: Union[str, None] = None
    done: bool
    importance: conint(ge=1, le=3)
    created: datetime


class TodoUpdate(TodoBase):
    title: Union[str, None] = None
    description: Union[str, None] = None
    done: Union[bool, None] = None
    importance: conint(ge=1, le=3) = None


class TodoInDb(TodoBase):
    id: int
    description: Union[str, None] = None
    done: bool
    importance: conint(ge=1, le=3)
    owner_id: int
    created: datetime


class UserBase(BaseModel):
    email: EmailStr
    username: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    active: bool
    created: datetime
    todos: list[Todo] = []


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
