from fastapi import APIRouter, Depends

depen=APIRouter()


async def common_parameteres(q:str | None=None, skip:int=0, limit:int=100):
    '''By calling this function we will be able to get the args of this function in another function too'''
    return {"q":q,"skip":skip,"limit":limit}


@depen.get('/items/')
async def read_items(common:dict=Depends(common_parameteres)):
    return common


@depen.get('/users/')
async def read_users(common:dict=Depends(common_parameteres)):
    return common
