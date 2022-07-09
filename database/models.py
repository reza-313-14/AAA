from database.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class DbAdmin(Base):
    __tablename__ = 'admins'
    id = Column('id', Integer, primary_key=True, index=True)
    username = Column('username', String)
    email = Column('email', String)
    password = Column('password', String)
    items = relationship('DbArticle', back_populates='admin')
    
    

class DbArticle(Base):
    __tablename__ = "articles"
    id = Column('id', Integer, primary_key=True, index=True)
    title = Column(String())
    content = Column(String())
    published = Column(Boolean())
    category = Column(String())
    admin_id = Column(Integer, ForeignKey("admins.id"))
    admin = relationship("DbAdmin", back_populates='items')