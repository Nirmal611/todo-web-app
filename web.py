import streamlit as st
import functions

st.title("My ToDo List:")
st.subheader("An app to increase your productivity !")
st.write('Current todo list :')

todos = functions.get_todos()
print(todos)

for index,todo in enumerate(todos) :
    checkbox = st.checkbox(todo,key=todo)
    if checkbox :
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()


def add_todo():
    todo = st.session_state['textbox'].strip()

    if not todo+'\n' in todos and todo != '':
        todos.append(todo+'\n')
        functions.write_todos(todos)

st.text_input(label='Enter a new todo:',placeholder='Enter a todo',on_change=add_todo,key='textbox')



print(st.session_state)
