import streamlit as st

st.set_page_config(page_title="To-Do App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do App")

new_task = st.text_input("New task", key="new_task")

if st.button("Add task"):
    task = new_task.strip()
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ""

st.subheader("Tasks")

if st.session_state.tasks:
    for index, task in enumerate(list(st.session_state.tasks)):
        cols = st.columns([0.85, 0.15])
        cols[0].write(task)
        if cols[1].button("Delete", key=f"delete_{index}"):
            st.session_state.tasks.pop(index)
            st.rerun()
else:
    st.info("No tasks yet. Add one above!")
