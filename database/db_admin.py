from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from schemas import AdminBase
from database.models import DbAdmin
from database.hash import Hash
from fastapi import status


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


def get_admin(id, db: Session):
    return db.query(DbAdmin).filter(DbAdmin.id == id).first()


def get_admin_by_username(username, db:Session):
    admins = db.query(DbAdmin).filter(DbAdmin.username == username).all()
    
    if not admins:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"admin with UserName {username} could not be found")
    
    return admins


def delete_admin(id, db:Session):
    admin = get_admin(id, db)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"admin with UserName {id} could not be found")
    
    db.delete(admin)
    db.commit()
    return {'message': f'admin {admin.username} deleted'}