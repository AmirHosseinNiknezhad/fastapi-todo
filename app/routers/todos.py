from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas, security
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=schemas.Todo)
def create_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
    current_user=Depends(security.get_current_active_user),
):
    return crud.create_user_todo(db=db, todo=todo, user_id=current_user.id)


@router.get("/", response_model=List[schemas.Todo])
def read_todos(
    db: Session = Depends(get_db),
    current_user=Depends(security.get_current_active_user),
):
    return crud.get_user_todos(user_id=current_user.id, db=db, skip=0, limit=100)


@router.put("/{todo_id}", response_model=schemas.Todo)
def update_todo(
    todo: schemas.TodoUpdate,
    todo_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(security.get_current_active_user),
):

    return crud.update_user_todo(
        db=db, todo_id=todo_id, new_todo=todo, owner_id=current_user.id
    )
