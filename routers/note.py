from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity

note=APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Notes.Notes.find({})
    newDocs=[]
    for doc in docs:
            newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "description":doc["description"]
        })
    print(newDocs)
    return templates.TemplateResponse("index.html", {"request":request,"newDocs":newDocs} )


@note.post('/',response_class=HTMLResponse)
async def add_item(note:Note):
    docs=conn.Notes.Notes.insert_one(dict(note))
    return noteEntity(docs)
