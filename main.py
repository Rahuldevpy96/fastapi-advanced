from fastapi import FastAPI
from routers.note import note
from fastapi.staticfiles import StaticFiles
from routers.user import MyMiddleware, user
from routers.todo import todo
from routers.extra import extra


app=FastAPI()
app.include_router(note,tags=['Notes'])
app.include_router(user,tags=['Users'])
app.include_router(todo,tags=['Todo'])
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(MyMiddleware)
app.include_router(extra,tags=['Extra_data'])