from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos


@router.post("/{user_id}/", response_model=schemas.Todo)
def create_user_todo(
    user_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)
):
    return crud.create_user_todo(db=db, todo=todo, user_id=user_id)
