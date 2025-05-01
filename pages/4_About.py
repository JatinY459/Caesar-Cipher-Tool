import streamlit as st
from app.app_config import apply_page_config

# page configuration
apply_page_config()

st.markdown("""
    <style>
    /* Completely hide all anchor link icons next to Streamlit headers */
    a.css-1dp5vir.e1g8pov64 {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)



st.title("About the App")