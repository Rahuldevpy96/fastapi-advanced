from fastapi import APIRouter
from config.db import conn
from models.todo import Todo
from schemas.todo import todo_serializer,todos_serializer

todo=APIRouter()

@todo.get('/get')
def get_todo():
    todo=todos_serializer(conn.Notes.todo.find())
    return {"status":"ok","data":todo}
