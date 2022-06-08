from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas, security
from ..database import get_db

router = APIRouter(prefix="/admin")


@router.get("/users", response_model=list[schemas.User], include_in_schema=False)
def read_users(
    current_user=Depends(security.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if not current_user.username == "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="ONLY ADMIN"
        )
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User, include_in_schema=False)
def read_user(
    user_id,
    current_user=Depends(security.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if not current_user.username == "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="ONLY ADMIN"
        )
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with the id of {user_id} not found",
        )
    return user


@router.patch(
    "/users/{user_id}",
    response_model=schemas.User,
    include_in_schema=False,
)
def toggle_active_user(
    user_id,
    current_user=Depends(security.get_current_active_user),
    db: Session = Depends(get_db),
):
    if not current_user.username == "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="ONLY ADMIN"
        )
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with the id of {user_id} not found",
        )
    crud.toggle_active_user_by_id(db, user_id)
    return user


@router.get("/todos", response_model=list[schemas.TodoInDb], include_in_schema=False)
def read_todos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(security.get_current_active_user),
):
    if not current_user.username == "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="ONLY ADMIN"
        )
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos
