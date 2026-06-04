import streamlit as st
import pandas as pd
from components.sidebar import sidebar

if "user" not in st.session_state:
    st.switch_page("login.py")

sidebar()

st.title("AgroVision Main Dashboard")

df = pd.read_csv("data/fields.csv")
st.dataframe(df)

field = st.selectbox("Select Field", df["field_name"])

if st.button("Open Field Analysis"):
    st.session_state["selected_field"] = field
    st.switch_page("pages/2_Field_Analysis.py")
