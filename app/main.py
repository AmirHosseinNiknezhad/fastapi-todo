from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

from . import security
from .routers import todos, users, admin

app = FastAPI()

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
