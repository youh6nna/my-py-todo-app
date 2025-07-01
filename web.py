import streamlit as st 
import functions

def add_todo():
    temp = st.session_state["text_key"]
    todo = temp + '\n'    
    todos = functions.get_todos()
    todos.append(todo) 
    functions.write_todos(todos)


st.title("My Web Todo App")

st.subheader("this is an app to increase your productivity")

todos = functions.get_todos()
for index , item in enumerate(todos):
    key = item + '\n'
    checkbox = st.checkbox(item ,key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()
    

st.text_input(label="Enter the todo : " ,placeholder="Do the todo" 
              , key="text_key" , on_change=add_todo)

st.session_state