import streamlit as st
import functions

st.session_state
todos = functions.get_todos()

def get_new_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("Python TO-DO List")
st.subheader(" This is my todo list app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    st.checkbox(todo, key=f"{index}_todo")

st.text_input(label="", placeholder=" Add your todo...",
                       on_change=get_new_todo,key='new_todo')










