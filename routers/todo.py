from bson import ObjectId
from fastapi import APIRouter
from config.db import conn
from models.todo import Todo
from schemas.todo import todo_serializer,todos_serializer

todo=APIRouter()

@todo.get('/get')
def get_todo():
    todo=todos_serializer(conn.Notes.todo.find())
    return {"status":"ok","data":todo}


@todo.post('/post')
def get_todo(todo:Todo):
    todos=conn.Notes.todo.insert_one(dict(todo))
    todo=todos_serializer(conn.Notes.todo.find({"_id":todos.inserted_id}))
    return ({"Stutus":"Success","data":todo})


@todo.put('/update/{id}')
def update_todo(id,todo:Todo):
    todos=conn.Notes.todo.find_one_and_update({"_id":(ObjectId(id))},{
        "$set":dict(todo)
    })
    todo=todos_serializer(conn.Notes.todo.find({"_id":ObjectId(id)}))
    return ({"Stutus":"Success","data":todo})

@todo.delete('/delete/{id}')
def update_todo(id,todo:Todo):
    conn.Notes.todo.find_one_and_delete({"_id":(ObjectId(id))})
    return ({"Stutus":"Success"})
