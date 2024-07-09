import streamlit as st 
import functions

def add_todo():
    todo=st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

todos=functions.get_todos()
st.title("MY TODO APP")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
count=0
for todo in todos:
    st.checkbox(todo,key=count)
    count+=1
    
    
st.text_input(label="add todo",placeholder="Add new todo....",
              on_change=add_todo,key="new_todo")    