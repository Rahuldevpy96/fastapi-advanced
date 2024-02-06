from bson import ObjectId
from fastapi import APIRouter, HTTPException,status
from config.db import conn
from models.todo import Todo
from schemas.todo import todo_serializer,todos_serializer

todo=APIRouter()

@todo.get('/todo')
def get_todo():
    '''This Function will get all the todo list
    If there is no data in  database than it will return a message "Data Not found".'''
    todo=todos_serializer(conn.Notes.todo.find())
    if todo:
        return {"status":"ok","data":todo}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )

@todo.get('/count_todos')
async def count_todos():
    '''This api will count all the todos.'''
    todo= todos_serializer(conn.Notes.todo.find())
    todos=len(todo)
    if todos:
        return {"status":"ok","data":todos
}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Something went wrong"
        )
@todo.get('/todo/{id}')
def get_todo_by_id(id):
    '''This function will return the particular todo data of given id.'''
    todo=todos_serializer(conn.Notes.todo.find({"_id":(ObjectId(id))}))
    if todo:
        return {"status":"ok","data":todo}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )

@todo.post('/todo')
def post_todo(todo:Todo):
    '''From this api we will be able to add new data. For that we need to add task_name and task_description'''
    todos=conn.Notes.todo.insert_one(dict(todo))
    todo=todos_serializer(conn.Notes.todo.find({"_id":todos.inserted_id}))
    if todo:
        return ({"status":"Success","data":todo})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data not saved"
        )


@todo.put('/todo/{id}/')
def update_todo(id,todo:Todo):
    '''From this api we can update the data of given id.'''
    updated=conn.Notes.todo.find_one_and_update({"_id":(ObjectId(id))},{
        "$set":dict(todo)
    })
    if updated:
        return ({"status":"Success","data":todo})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data not updated"
        )


@todo.delete('/todo/{id}/')
def delete_todo(id):
    '''This api will delete the data of given id.'''
    deleted=conn.Notes.todo.find_one_and_delete({"_id":(ObjectId(id))})
    if deleted:
        return ({"status":"Success",'data':"Data Deleted Successfully"})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data not deleted"
        )
