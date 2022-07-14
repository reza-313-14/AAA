from sqlalchemy import and_
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from database.models import DbArticle
from schemas import ArticleBase
from fastapi import status


def create_article(db: Session, request: ArticleBase, article_category):
    article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        category = article_category,
        admin_id = request.creator_id
        )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(id, db:Session):
    article = db.query(DbArticle).filter(and_(DbArticle.id == id, DbArticle.published == True)).first()
    
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"article with id {id} could not be found")
    
    return article



def get_all_articles(db:Session):
    return db.query(DbArticle).filter(DbArticle.published == True).all()


def delete_article(id, db:Session):
    article = get_article(id, db)
    
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"article with id {id} could not be found")
    
    db.delete(article)
    db.commit()
    return {'message': f'article {article.id} deleted'}