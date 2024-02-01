import time
from fastapi import APIRouter
from fastapi import BackgroundTasks
from pydantic import EmailStr

extra=APIRouter()
def write_notifucation(email:str,message=str):
    with open('log.text',mode='a') as email_file:
        content=f"Notification for \n{email}: {message}\n"
        time.sleep(5)
        email_file.write(content)

@extra.post('/extra_task')
async def send_notification(email:EmailStr,message:str,background_task:BackgroundTasks):
    '''By using this api we will be able to add some message for particular email and that message will save in text file'''
    background_task.add_task(write_notifucation,email,message)
    return {"message":"Notification sent in the background"}
