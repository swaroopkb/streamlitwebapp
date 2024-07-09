import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new todo"]
    todos.append(new_todo + "\n")
    functions.write_todos(todos)


st.title("My first web app")
st.subheader("this is my todo app")

st.write("This app is for learning python")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="add a todo",
              on_change=add_todo, key="new todo")
st.button(label="Add todo")
