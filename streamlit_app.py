import streamlit as st
from app.cipher import *
from app.app_config import apply_page_config

# page configuration
apply_page_config()

st.title("Caesar Cipher Encryption/Decryption 🔏")
st.write("This app allows you to encrypt and decrypt messages using the Caesar cipher.")
