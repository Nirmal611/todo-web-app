def get_todos():
    with open('todos.txt','r') as file:
        todo=file.readlines()
        return todo


def write_todos(todos):
    with open('todos.txt','w') as file:
        file.writelines(todos)



