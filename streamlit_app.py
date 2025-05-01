import streamlit as st
from app.cipher import *

st.set_page_config(
    page_title="Cipher Playground",
    page_icon="🔏",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://streamlit.io",
        "Report a bug": "https://github.com/yourproject/issues",
        "About": "### Cipher Playground\nPlay with the Classic Caesar Cipher\nMade by Jatin Yadav!"
    }
)

st.title("Caesar Cipher Encryption/Decryption 🔏")
st.write("This app allows you to encrypt and decrypt messages using the Caesar cipher.")
