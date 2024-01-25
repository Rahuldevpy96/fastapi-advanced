import secrets
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from passlib.hash import bcrypt
from passlib.handlers.bcrypt import bcrypt
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.templating import Jinja2Templates
from config.db import conn
from models.user import User
from schemas.user import userEntity,usersEntity

user=APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="templates")
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"


@user.get('/users')
async def find_all_users():
    '''This api will show all the users.'''
    user= usersEntity(conn.Notes.user.find())
    if user:
        return {"status":"ok","data":[{'id': item['id'], 'name': item['username'], 'email': item['email']} for item in user]
}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )


async def create_users(user:User):
    '''From this api we will be able to add new user.'''
    user_data = user.dict()
    print(user_data)
    user_data["hashed_password"] = bcrypt.hash(user_data["hashed_password"])
    result = conn.Notes.user.insert_one(user_data)
    return result

    
async def get_user(username: str):
    user = conn.Notes.user.find_one({"username": username})
    return user

async def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return username

@user.post("/register")
async def register(user: User):
    await create_users(user)
    return {"message": "User registered successfully"}

# Endpoint to create a new token
@user.post("/token")
async def create_token(username: str, password: str):
    user = await get_user(username)
    if user and bcrypt.verify(password, user["hashed_password"]):
        # Token expiration time: 30 minutes (adjust as needed)
        expire_time = 30  # minutes
        token_data = {"sub": username, "exp": expire_time}
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

# Protected endpoint that requires a valid token
@user.get("/protected")
async def get_protected_data(current_user: str = Depends(verify_token)):
    return {"message": "This is protected data", "current_user": current_user}


@user.put('/user/{id}')
async def update_user(id,user:User):
    '''After providing the id we will be able to edit the user details.'''
    user=conn.Notes.user.find_one_and_update({"_id":(ObjectId(id))},{
        "$set":dict(user)
    })
    print(user)
    if user:
        return {"status":"ok","name":user['username'],"email":user['email']
}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to update data"
        )


@user.delete('/user/{id}')
async def delete_user(id,user:User):
    '''This api will delete the user of given id.'''
    user= userEntity(conn.Notes.user.find_one_and_delete({"_id":(ObjectId(id))}))
    if user:
        return {"status":"ok","data":"Data Deleted Successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not deleted"
        )


@user.get('/user/{id}')
def get_user_by_id(id):
    '''This function will return the particular user data of given id.'''
    user=usersEntity(conn.Notes.user.find({"_id":(ObjectId(id))}))
    if user:
        return {"status":"ok","data":[{'id': item['id'], 'name': item['username'], 'email': item['email']} for item in user]
}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Data Not found"
        )
    