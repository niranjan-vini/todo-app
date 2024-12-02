import streamlit as sg
import function

def add():
    todo=sg.session_state["add"]+"\n"
    item.append(todo)
    function.new(item)

sg.title("my_app")
sg.subheader("small app")
sg.write("hello python world iam niranjan")

item=function.old()

for index, todos in enumerate(item):
    box=sg.checkbox(todos,key=todos)
    if box:
        item.pop(index)
        function.new(item)
        del sg.session_state[todos]


sg.text_input(placeholder="add new todo",label="hello world",on_change=add,key="add")

print("hi")
sg.session_state