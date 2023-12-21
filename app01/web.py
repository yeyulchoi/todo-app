import streamlit as st
import functions



st.title("Python TO-DO List")
st.subheader(" This is my todo list app")
st.write("This app is to increase your productivity")

todos= functions.get_todos()
for todo in todos:
    st.checkbox(todo)

new_todo=st.text_input(label="Enter todo", placeholder=" Add your todo")
print(new_todo)




