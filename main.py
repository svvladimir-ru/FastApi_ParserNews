from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from parser import schemas, crud, models
from parser.bd import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def create_resurs(resurs: schemas.ResursCreate, db: Session = Depends(get_db)):
    return crud.create_resurs(db=db, resurs=resurs)


"""Создаем ресурсы"""
create_resurs(resurs='lenta')
create_resurs(resurs='interfax')
create_resurs(resurs='kommersant')
create_resurs(resurs='m24')


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
