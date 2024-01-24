from bson import ObjectId
from fastapi import APIRouter, HTTPException,status
from fastapi.templating import Jinja2Templates
from config.db import conn
from models.user import User
from schemas.user import userEntity,usersEntity

user=APIRouter()
templates = Jinja2Templates(directory="templates")


@user.get('/users')
async def find_all_users():
    '''This api will show all the users.'''
    user= usersEntity(conn.Notes.user.find())
    if user:
        return {"status":"ok","data":user}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )


@user.post('/users')
async def create_users(user:User):
    '''From this api we will be able to add new user.'''
    users=conn.Notes.user.insert_one(dict(user))
    user= usersEntity(conn.Notes.user.find({"_id":users.inserted_id}))
    if user:
        return {"status":"ok","data":user}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )


@user.put('/user/{id}')
async def update_user(id,user:User):
    '''After providing the id we will be able to edit the user details.'''
    conn.Notes.user.find_one_and_update({"_id":(ObjectId(id))},{
        "$set":dict(user)
    })
    user= userEntity(conn.Notes.user.find_one({"_id":(ObjectId(id))}))
    if user:
        return {"status":"ok","data":user}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )


@user.delete('/user/{id}')
async def delete_user(id,user:User):
    '''This api will delete the user of given id.'''
    user= userEntity(conn.Notes.user.find_one_and_delete({"_id":(ObjectId(id))}))
    if user:
        return {"status":"ok","data":"Data Deleted Successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User Not found"
        )


@user.get('/user/{id}')
def get_user_by_id(id):
    '''This function will return the particular user data of given id.'''
    user=usersEntity(conn.Notes.user.find({"_id":(ObjectId(id))}))
    if user:
        return {"status":"ok","data":user}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )
    