import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    txtbox_todo = st.session_state['new_todo'] + "\n"
    todos.append(txtbox_todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

checkbox_index = 0
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=checkbox_index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[checkbox_index]
        st.experimental_rerun()
    checkbox_index = checkbox_index + 1

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
