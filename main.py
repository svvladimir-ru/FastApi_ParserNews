import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from parser import schemas, crud, models
from parser.db import SessionLocal, engine
from parser.parser import Graber


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app = FastAPI()
graber = Graber()
item_lenta = graber.lenta.news(3)


@app.get('/news')
def get_news(item_lenta=item_lenta):
    return f'lenta:\n{graber.lenta.news(3)}\n\n' \
           f'interfax:\n{graber.interfax.news(3)}\n\n' \
           f'kommersant:\n{graber.kommersant.news(3)}\n\n' \
           f'm24:\n{graber.m24.news(3)}'


# @app.post("/resurs/", response_model=schemas.Resurs)
# """Создаем новостные ресурсы"""
# def create_resurs(resurs: schemas.ResursCreate, db: Session = Depends(get_db)):
#     return crud.create_resurs(db=db, resurs=resurs)


# def create_item_for_user(
#     resurs_id: int, item: schemas.ItemCreate
# ):
#     return crud.create_resurs_item(item=item, resurs_id=resurs_id)


# z = Graber()
# a = z.lenta.news(3)
# for i in a:
# """Добавление информации в базу"""
#     create_item_for_user(resurs_id=1, item=i)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
