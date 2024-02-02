from fastapi import APIRouter, Depends

depen=APIRouter()


async def common_parameteres(q:str | None=None, skip:int=0, limit:int=100):
    return {"q":q,"skip":skip,"limit":limit}


@depen.get('/items/')
async def read_items(common:dict=Depends(common_parameteres)):
    return common


@depen.get('/users/')
async def read_users(common:dict=Depends(common_parameteres)):
    return common
