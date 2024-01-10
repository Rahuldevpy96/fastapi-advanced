from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


conn=MongoClient("mongodb+srv://kneha5489:rdslJF2rCMp8PqCM@cluster0.dwxshzd.mongodb.net")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Notes.Notes.find({})
    newDocs=[]
    for doc in docs:
        if "Notes" in doc:
            newDocs.append({
            "id":doc["_id"],
            "Notes":doc["Notes"]
        })
        else:
            newDocs.append({
                "id":doc["_id"]
            })
    print(newDocs)
    return templates.TemplateResponse("index.html", {"request":request,"newDocs":newDocs} )

