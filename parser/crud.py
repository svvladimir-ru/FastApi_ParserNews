from sqlalchemy.orm import Session
from parser import schemas, models
from parser.db import SessionLocal, engine


ses = SessionLocal()  # отдельная сессия для добавление данных в базу


def get_resurs(db: Session, resurs_id: int):
    """Получаем один ресурс"""
    return db.query(models.Resurs).filter(models.Resurs.id == resurs_id).first()


def get_full_resurs(db: Session, skip: int = 0, limit: int = 4):
    """Все ресурсы"""
    return db.query(models.Resurs).offset(skip).limit(limit).all()


def create_resurs(db: Session, resurs: schemas.ResursCreate):
    """Создаем ресурс(имя новостного канала)"""
    db_resurs = models.Resurs(name_resurs=resurs.name_resurs)
    db.add(db_resurs)
    db.commit()
    db.refresh(db_resurs)
    return db_resurs


def get_items(db: Session, skip: int = 0, limit: int = 3):
    """Получаем новости из таблицы"""
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_resurs_item(item: schemas.ItemCreate, resurs_id: int):
    """Добавляем новости в таблицу"""
    db_item = models.Item(**item, resurs_id=resurs_id)
    ses.add(db_item)
    ses.commit()
    ses.refresh(db_item)
    return db_item
