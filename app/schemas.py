from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, EmailStr, conint


class TodoBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


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
    title: Optional[str]
    description: Optional[str]
    done: Optional[bool]
    importance: Optional[conint(ge=1, le=3)]


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
        orm_mode = True


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
