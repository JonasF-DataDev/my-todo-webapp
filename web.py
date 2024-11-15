# De bovenste 2 lijnen maken de webapp (import + st.title)
import streamlit as st
import functions

# Lijst met todos ophalen
todos = functions.get_todos()

# nieuwe todo in variabele steken, toevoegen aan todos, pushen naar txtfile en textvak leegmaken
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.push_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Voor elke to-do in todos maakt die een checkbox aan
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.push_todos(todos)
        del st.session_state[todo]
        st.rerun()

# DIt is het tekstvakje onderaan dat we identificeren met key "new_todo"
st.text_input(label="Add new todo", label_visibility="hidden", placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')


