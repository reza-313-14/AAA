from fastapi import APIRouter, FastAPI
from fastapi.requests import Request
from database.db import get_db


app = FastAPI()




@app.middleware('http')
async def logs(request: Request, call_next):
    
    log = f"""
    -------------log-----------
    host : {request.client.host}
    port : {request.client.port}
    url : {request.url}
    method : {request.method}
    """
    
    with open('log.txt', 'a') as file:
        file.write(log)
        file.close()
    
    response = await call_next(request)
    return response