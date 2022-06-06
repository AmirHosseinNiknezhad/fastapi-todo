from datetime import datetime
from typing import Union

from pydantic import BaseModel, EmailStr, conint


class TodoBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    description: Union[str, None] = None
    done: bool = False
    importance: conint(ge=1, le=3) = 1


class UserBase(BaseModel):
    email: EmailStr
    username: str

    class Config:
        orm_mode = True


class Todo(TodoBase):
    id: int
    description: Union[str, None] = None
    done: bool
    importance: conint(ge=1, le=3)
    owner_id: int
    owner: UserBase
    created: datetime


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    active: bool
    created: datetime
    todos: list[Todo] = []


class UserInDB(UserBase):
    password: str
    id: int
    active: bool
    created: datetime
    todos: list[Todo] = []


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
