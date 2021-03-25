from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON
from .bd import Base, engine
from sqlalchemy.orm import relationship


class Resurs(Base):
    __tablename__ = 'resurs'

    id = Column(Integer, primary_key=True, index=True)
    name_resurs = Column(String(30))
    items = relationship("Item", back_populates="news_resurs")

    def __repr__(self):
        return f'<Resurs(name="{self.name_resurs}")>'


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150))
    link = Column(String(200))
    description = Column(Text)
    pubdate = Column(String(50))
    image = Column(String(200))
    category = Column(String(20))
    genre = Column(String(100))
    media = Column(String(100))
    full_item = Column(JSON)
    resurs_id = Column(Integer, ForeignKey("resurs.id"))
    news_resurs = relationship("Resurs", back_populates="items")


# Resurs.__table__
# Item.__table__
# Base.metadata.create_all(engine)