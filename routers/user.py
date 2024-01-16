from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from config.db import conn
from models.user import User
from schemas.user import userEntity,usersEntity

user=APIRouter()
templates = Jinja2Templates(directory="templates")


@user.get('/users')
async def find_all_users():
    return usersEntity(conn.Notes.user.find())


@user.post('/users')
async def create_users(user:User):
    users=conn.Notes.user.insert_one(dict(user))
    return usersEntity(conn.Notes.user.find())
