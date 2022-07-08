from fastapi import APIRouter, Depends
from schemas import AdminBase, AdminDisplay
from database.db import get_db
from database import db_admin

router = APIRouter(prefix='/admin', tags=['admin'])


# admin register
@router.post("/register", response_model=AdminDisplay)
def register(admin: AdminBase, db= Depends(get_db)):
    return db_admin.create_admin(db, admin)