from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from . import security
from app.config import SETTINGS
from .routers import todos, users, admin

app = FastAPI()

origins = SETTINGS.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(security.router)
app.include_router(users.router)
app.include_router(todos.router)
app.include_router(admin.router)


@app.get("/", tags=["Home"])
def welcome():
    html_content = """
    <h1>Welcome! click <a href="/docs">here</a> for the documentation!</h1>
    """
    return HTMLResponse(content=html_content, status_code=200)
