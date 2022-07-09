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
    # style 1
    return db_admin.get_admin(id, db)


# get admin by username
@router.get('/admin/username/{username}', response_model=List[AdminDisplay])
def get_admin_by_username(username: str, db= Depends(get_db)):
    return db_admin.get_admin_by_username(username, db)


# delete admin
@router.get('/delete/{id}')
def delete_admin(id: int, db= Depends(get_db)):
    return db_admin.delete_admin(id, db)


# update admin
@router.post('/update/{id}')
def update_admin(id: int, admin: AdminBase ,db= Depends(get_db)):
    return db_admin.update_admin(id, db, admin)