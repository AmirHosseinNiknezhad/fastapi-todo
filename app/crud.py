from pydoc import describe
from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.Todo(**todo.model_dump(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def get_user_todos(user_id: int, db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Todo)
        .filter(models.Todo.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_todo_by_id(id: int, db: Session):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def update_todo(
    id: int,
    new_todo: schemas.TodoUpdate,
    db: Session,
):
    query = db.query(models.Todo).filter(models.Todo.id == id)
    request_feilds = new_todo.model_dump()
    updates = {k: v for k, v in request_feilds.items() if v is not None}
    query.update(updates, synchronize_session=False)
    db.commit()
    return query.first()


def delete_todo(id: int, db: Session):
    query = db.query(models.Todo).filter(models.Todo.id == id).delete()
    db.commit()


def toggle_active_user_by_id(db: Session, user_id: int):
    current_status = (
        db.query(models.User).filter(models.User.id == user_id).first().active
    )
    db.query(models.User).filter(models.User.id == user_id).update(
        {"active": not current_status}, synchronize_session=False
    )
    db.commit()
    return
