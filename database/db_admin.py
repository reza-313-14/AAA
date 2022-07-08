from sqlalchemy.orm.session import Session
from schemas import AdminBase
from database.models import DbAdmin
from database.hash import Hash


def create_admin(db:Session, request:AdminBase):
    
    if "@gmail.com" not in request.email:
        # raise EmailNotValid("Email Not Valid!")
        pass
    
    admin = DbAdmin(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


def get_all_admins(db:Session):
    return db.query(DbAdmin).all()