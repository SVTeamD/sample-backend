from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from backend.models.models import Order

from models import crud, models, schemas
from models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# juwon_Order

<<<<<<< main
########################################

@app.post("/menus/", response_model = schemas.Menu) # menu_id는 누가 입력할지 -> 사장 or 자동
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu = menu)


@app.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_menu(db)
    return menus


@app.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, menu_id=menu_id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name=menu_name)
    return menus


@app.delete("/menus/{menu_name}")
def delete_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    response = crud.delete_menu(db, menu_name = menu_name)
    return response.status_code


=======

@app.get("/users/order/", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    Order = crud.get_user(db, order_id=order_id)
    return Order


@app.post("/users/order/", response_model=schemas.Order)
def create_order(
    order_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, order_id=order_id)
>>>>>>> feat: start writing order api
