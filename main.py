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

@app.get('/')
def get_resurs():
    return f'Добрый день!            ' \
           f'Прошу прощения за эту халтуру(обходной вариант)), так как смог уделить всего 15ч задаче       ' \
           f'Из которых час потратил на работу с декодом парсера Interfax(решил проблему заменив:' \
           f'BeautifulSoup(get_html(url).text на BeautifulSoup(get_html(url).content.....      ' \
           f'И 5ч потратил на то что бы подключить хоть какую-то базу. Проблема была решена обновлением Sqlalcemy' \
           f'c 1.3.22 на 1.4(даже sqllite не подключал...)), остальное время потратил на изучение fastapi, pydantic' \
           f'Присылаю этот "обходной вариант", так как в условие не сказано что данные должны записываться и получаться ' \
           f'из бд. Запись в бд реализовал, а вот вытащить не успел.' \
           f'Буду рад обратной связи. Тел. +79032644045                                               ' \
           f'                                      url для просмотра данный /news' \


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
