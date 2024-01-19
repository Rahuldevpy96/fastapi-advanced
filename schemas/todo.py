def todo_serializer(todo)->dict:
    return{
        "id":str(todo["_id"]),
        "task_name":todo["task_name"],
        "task_description":todo["task_description"],
    }


def todos_serializer(todos)->list:
    return [todo_serializer(todo) for todo in todos ]