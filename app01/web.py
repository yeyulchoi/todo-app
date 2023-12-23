import streamlit as st
import functions


todos = functions.get_todos()

def get_new_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state.new_todo = ""

st.title("Python TO-DO List")
st.subheader(" This is Yeyul's todo list app")
st.write("This app is to increase your productivity")

st.text_input(label="", placeholder=" Add your todo...",
                       on_change=get_new_todo,key='new_todo')

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()












