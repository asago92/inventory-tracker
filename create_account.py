import streamlit as st

def create_account():
    st.title("Create your account")

pg = st.navigation([
    st.Page("create_account.py", title="First page", icon="🔥"),
])
pg.run()
