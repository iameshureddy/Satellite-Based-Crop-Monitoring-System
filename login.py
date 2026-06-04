import streamlit as st
import pandas as pd

st.title("AgroVision Login")

users_df = pd.read_csv("data/users.csv")

u = st.text_input("Username")
p = st.text_input("Password", type="password")

if st.button("Login"):
    user = users_df[(users_df.username==u) & (users_df.password==p)]

    if not user.empty:
        st.session_state["user"] = u
        st.session_state["role"] = user.iloc[0]["role"]
        st.switch_page("app.py")
    else:
        st.error("Invalid login")

st.page_link("signup.py", label="Create new account")
