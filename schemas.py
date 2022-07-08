from pydantic import BaseModel


class AdminBase(BaseModel):
    username: str
    password: str
    email: str
    
    

class AdminDisplay(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True