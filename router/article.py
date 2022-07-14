from typing import List
from fastapi import APIRouter, Depends
from database import db_article
from database.db import get_db
from schemas import ArticleBase, ArticleDisplay
from fastapi import File, UploadFile
from enum import Enum



router = APIRouter(prefix='/article', tags=['article'])


class ArticleCategory(str, Enum):
    lang1 = "Python"
    lang2 = "JavaScript"
    lang3 = "Java"
    lang4 = "Kotlin"
    lang5 = "Php"
    lang6 = "C++"



# create article
@router.post('/create', response_model=ArticleDisplay)
def create_article(article: ArticleBase, articleCategory: ArticleCategory, db= Depends(get_db)):
    print(articleCategory)
    print(article)
    print(db)
    return db_article.create_article(db=db, request=article, article_category=articleCategory)


@router.get('/get/{id}', response_model=ArticleDisplay)
def get_article(id: int, db= Depends(get_db)):
    return db_article.get_article(id, db)



@router.get('/all', response_model=List[ArticleDisplay])
def get_all_articles(db= Depends(get_db)):
    return db_article.get_all_articles(db)


@router.get('/delete/{id}')
def delete_artice(id: int, db= Depends(get_db)):
    return db_article.delete_article(id, db)