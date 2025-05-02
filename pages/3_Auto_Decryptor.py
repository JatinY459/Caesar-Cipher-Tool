import streamlit as st
from app.cipher import caesar_decrypt_auto
from app.app_config import apply_page_config
from app.utils import apply_btn_styles, add_nav_buttons

# page configuration
apply_page_config()
apply_btn_styles()

st.title("Caesar Cipher Auto Decryptor 🔓")
st.markdown("Decipher your messages using the Caesar cipher automatically by just entering your message!<br>This Auto Decryptor gives you the most likely deciphered message using a list of 3000 most common words in English.", unsafe_allow_html=True)
st.markdown("<span style='font-weight: 900;'>Note:</span> This Auto Decryptor works best with common English text. If you are using a different language or a complex English message, please use the Brute Force Decryptor instead.", unsafe_allow_html=True)

# Input field & its variable
message = st.text_input("Enter your message:", key="message", placeholder="your message")

if st.button("Decrypt Automatically"):
    if message == "":
        st.warning("Please enter a message to decrypt.")
    else:
        decrypted_message = caesar_decrypt_auto(message)
        if decrypted_message:
            st.write(f"""### Caesar Cipher Decryption of Your Message is:
                     {decrypted_message}""")
        else:
            st.write("No valid words found in the decrypted message. Please try again with a different message.")

add_nav_buttons("Auto_Decryptor")