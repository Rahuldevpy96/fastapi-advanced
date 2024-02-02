from fastapi import APIRouter

depen=APIRouter()


@depen.get('/items/')
async def read_items(q:str | None=None, skip:int=0, limit:int=100):
    return {"q":q,"skip":skip,"limit":limit}
