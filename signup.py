import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Signup", layout="centered")

st.title("📝 AgroVision Signup")

file = Path("data/users.csv")

if not file.exists():
    df = pd.DataFrame(columns=["username","password","role"])
    df.to_csv(file, index=False)

users_df = pd.read_csv(file)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
role = st.selectbox("Role", ["farmer","admin"])

if st.button("Create Account"):
    if username in users_df["username"].values:
        st.error("Username already exists")
    else:
        new_user = pd.DataFrame([[username,password,role]],
                                columns=["username","password","role"])
        users_df = pd.concat([users_df,new_user])
        users_df.to_csv(file, index=False)
        st.success("Account created successfully")
