from database.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class DbAdmin(Base):
    __tablename__ = 'admins'
    id = Column('id', Integer, primary_key=True, index=True)
    username = Column('username', String)
    email = Column('email', String)
    password = Column('password', String)