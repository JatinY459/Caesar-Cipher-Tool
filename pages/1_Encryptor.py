import streamlit as st
from app.cipher import caesar_shift

st.title("Caesar Cipher Encryptor 🔏")
st.write("Encrypt your messages using the Caesar cipher using a custom shift value!")

# Input fields and their variables
message = st.text_input("Enter your message:", key="message", placeholder="your message")
shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, placeholder="Shift value", value=1, key="shift")

if st.button("Encrypt"):
    if message == "":
        st.warning("Please enter a message to encrypt.")
    else:
        st.write(f"""### Caesar Cipher Encryption of Your Message is:
                 {caesar_shift(message, shift)}""")
        # st.write("### Caesar Cipher Encryption of Your Message is:")
        # encrypted_message = caesar_shift(message, shift)
        # st.write(f"## {encrypted_message}")