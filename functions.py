FILEPATH = "todos.txt"
import time

def nowtime():
    new = str(time.strftime("%b %d, %Y %H:%M"))
    return new

def get_todos(filepath = FILEPATH):
    with open(filepath,'r') as file:
        todos = file.readlines()
        
    return todos

def write_todos(todos_arg, filepath = FILEPATH):
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

