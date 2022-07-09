from fastapi import APIRouter, Depends
from requests import Session
from schemas import AdminBase, AdminDisplay
from database.db import get_db
from database import db_admin
from typing import List
from fastapi.exceptions import HTTPException
from fastapi import status


router = APIRouter(prefix='/admin', tags=['admin'])


# admin register
@router.post("/register", response_model=AdminDisplay)
def register(admin: AdminBase, db= Depends(get_db)):
    return db_admin.create_admin(db, admin)


# get all admin
@router.get('/admins', response_model=List[AdminDisplay])
def get_all_admins(db= Depends(get_db)):
    return db_admin.get_all_admins(db)


# get admin
@router.get('/admin/{id}', response_model=AdminDisplay)
def get_admin_by_id(id: int, db= Depends(get_db)):
    # style
    admin = db_admin.get_admin(id, db)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'admin with ID {id} could not be found')
    
    return admin


# get admin by username
@router.get('/admin/username/{username}', response_model=List[AdminDisplay])
def get_admin_by_username(username: str, db= Depends(get_db)):
    return db_admin.get_admin_by_username(username, db)