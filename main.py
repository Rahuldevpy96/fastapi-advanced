from fastapi import FastAPI
from routers.note import note
from fastapi.staticfiles import StaticFiles
from routers.user import user
from routers.todo import todo
from routers.form import form


app=FastAPI()
app.include_router(note,tags=['Notes'])
app.include_router(user,tags=['Users'])
app.include_router(todo,tags=['Todo'])
app.include_router(form,tags=['Language'])
app.mount("/static", StaticFiles(directory="static"), name="static")




