from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
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


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(security.get_current_active_user),
):
    current_todo: schemas.TodoInDb = crud.get_todo_by_id(db=db, id=todo_id)
    if not current_todo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo either not found or belongs to another user",
        )
    if not current_todo.owner_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo either not found or belongs to another user",
        )
    return crud.delete_todo(db=db, id=todo_id)


@router.patch("/{todo_id}", response_model=schemas.Todo)
def update_todo(
    todo: schemas.TodoUpdate,
    todo_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(security.get_current_active_user),
):
    current_todo: schemas.TodoInDb = crud.get_todo_by_id(db=db, id=todo_id)
    if not current_todo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo either not found or belongs to another user",
        )
    if not current_todo.owner_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo either not found or belongs to another user",
        )
    return crud.update_todo(db=db, id=todo_id, new_todo=todo)
