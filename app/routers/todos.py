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
