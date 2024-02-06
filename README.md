http://localhost:8000/users ->This api will show all the users.

http://localhost:8000/count_users ->This api will count all the users.

http://localhost:8000/register ->From this api we will be able to add new user. For that we have to enter username, email, hashed_password

http://localhost:8000/user/{id} ->After providing the id we will be able to edit the user details.

http://localhost:8000/user/{id} -> This api will delete the user of given id.

http://localhost:8000/user/{id} -> This function will return the particular user data of given id.

http://localhost:8000/user/middleware -> Here i have added a middleware



http://localhost:8000/todo ->This Function will get all the todo list. If there is no data in  database than it will return a message "Data Not found".

http://localhost:8000/todo ->From this api we will be able to add new data. For that we need to add task_name and task_description

http://localhost:8000/count_todos ->This api will count all the todos.

http://localhost:8000/todo/{id} ->This function will return the particular todo data of given id.

http://localhost:8000/todo/{id} -> From this api we can update the data of given id.

http://localhost:8000/todo/{id} ->This api will return the data of given id.
