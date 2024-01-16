from fastapi import FastAPI
from routers.note import note
from fastapi.staticfiles import StaticFiles
from routers.user import user


app=FastAPI()
app.include_router(note,tags=['Notes'])
app.include_router(user,tags=['Users'])
app.mount("/static", StaticFiles(directory="static"), name="static")




