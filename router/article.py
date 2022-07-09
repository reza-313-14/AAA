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