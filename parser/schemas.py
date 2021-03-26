from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    author: str
    title: str
    description: str
    link: str
    pubdate: str
    image: str = None
    category: str = None
    genre: str = None
    media: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    resurs_id: int

    class Config:
        orm_mode = True
    pass


class ResursBase(BaseModel):
    name_resurs: str


class ResursCreate(ResursBase):
    pass


class Resurs(ResursBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
