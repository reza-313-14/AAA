from email.mime import image
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from database.models import DbArticle
from schemas import ArticleBase


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