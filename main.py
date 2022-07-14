from fastapi import FastAPI
from fastapi.requests import Request
from database.db import get_db
from router import admin, article
from database import models
from database.db import engine


models.Base.metadata.create_all(engine)

app = FastAPI(
    title="my app",
    description="description of my app",
    version="1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
    redoc_url=None
)

app.include_router(admin.router)
app.include_router(article.router)



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