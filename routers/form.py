from typing import Annotated
from config.db import conn
from fastapi import Form,APIRouter

form = APIRouter()


@form.post("/form/")
async def form_test(Language: Annotated[str, Form()], type: Annotated[str, Form()]):
    return {"Language": Language}