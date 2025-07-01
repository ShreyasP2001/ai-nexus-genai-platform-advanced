import streamlit as st

def login_form():
    """Simple demo login form. Replace with secure method in production."""
    with st.sidebar.form("Login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if username == "admin" and password == "admin123":
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid credentials")
            st.session_state["authenticated"] = False

    return st.session_state.get("authenticated", False)
