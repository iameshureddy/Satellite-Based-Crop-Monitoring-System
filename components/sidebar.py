import streamlit as st

def sidebar():
    st.sidebar.title("AgroVision")
    st.sidebar.write("Satellite Crop Monitoring System")

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.switch_page("login.py")
