from pydantic import BaseModel

class Todo(BaseModel):
    task_name:str
    task_description:str
