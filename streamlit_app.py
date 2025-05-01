import streamlit as st

from app.cipher import *

st.title("Caesar Cipher Encryption/Decryption 🔏")
st.write("This app allows you to encrypt and decrypt messages using the Caesar cipher.")




message = st.text_input("Enter your message:", key="message", placeholder="your message")
shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, placeholder="Shift value", value=1, key="shift")


st.write("## Encryption")
if st.button("Encrypt"):
    if message == "":
        st.warning("Please enter a message to encrypt.")
    else:
        encrypted_message = caesar_shift(message, shift)
        st.write("Encrypted message:", encrypted_message)

st.write("## Brute Force Decryption")
if st.button("Decrypt"):
    if message == "":
        st.warning("Please enter a message to decrypt.")
    else:
        decrypted_messages = caesar_decrypt_brute(message)
        st.write("Possible decrypted messages:")
        col1, col2 = st.columns(2)
        col1.header("Shift Value")
        col2.header("Possible Message")
        for i, msg in enumerate(decrypted_messages):
            col1.write(str(i + 1))
            col2.write(msg)

st.write("## Auto Decryption")
if st.button("Auto Decrypt"):
    if message == "":
        st.warning("Please enter a message to decrypt.")
    else:
        decrypted_messages = caesar_decrypt_auto(message)
        st.write("Possible decrypted messages:")
        col1, col2 = st.columns(2)
        col1.header("Shift Value")
        col2.header("Possible Message")
        for i, msg in enumerate(decrypted_messages):
            col1.write(str(i + 1))
            col2.write(msg)