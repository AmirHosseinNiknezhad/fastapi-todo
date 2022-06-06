from fastapi import FastAPI

from . import security
from .routers import todos, users

app = FastAPI()

app.include_router(security.router)
app.include_router(users.router)
app.include_router(todos.router)
