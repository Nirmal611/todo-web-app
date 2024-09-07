def get_todos():
    with open('C:/Users/pnirm/PycharmProjects/ToDoListGUIapp/.venv/todos.txt','r') as file:
        todo=file.readlines()
        return todo


def write_todos(todos):
    with open('C:/Users/pnirm/PycharmProjects/ToDoListGUIapp/.venv/todos.txt','w') as file:
        file.writelines(todos)



