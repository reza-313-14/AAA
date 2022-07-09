from email.mime import image
from unicodedata import category
from fastapi import UploadFile, File
from pydantic import BaseModel
from enum import Enum

# Admin
class AdminBase(BaseModel):
    username: str
    password: str
    email: str
    
    

class AdminDisplay(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        orm_mode = True



class Admin(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True


# Article      




class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int
    
    
    
class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    category: str
    admin: Admin
    class Config:
        orm_mode = True