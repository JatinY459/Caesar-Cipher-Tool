import streamlit as st
from app.cipher import caesar_decrypt_brute
from app.app_config import apply_page_config
from app.utils import apply_btn_styles, add_nav_buttons

# page configuration
apply_page_config()
apply_btn_styles()

st.title("Brute Force Decryptor 🔓")
st.markdown("Decipher your messages using the Caesar cipher with brute force!<br>This Brute Force Decryptor gives you all the possible messages using all the shift values from 1 to 25.<br>And one of these messages is the real Decipher-ed message.", unsafe_allow_html=True)

# Input field & its variable
message = st.text_input("Enter your message:", key="message", placeholder="your message")

if st.button("Decrypt with Brute Force"):
    if message == "":
        st.warning("Please enter a message to decrypt.")
    else:
        decrypted_messages = caesar_decrypt_brute(message)
        st.header("Possible decrypted messages:")
        # col1, col2 = st.columns(2)
        # col1.write("#### Shift Value")
        # col2.write("#### Possible Message")
        # for i, msg in enumerate(decrypted_messages):
        #     col1.write(str(i + 1))
        #     col2.write(msg)

        table_data = [{
            "Shift Value": str(i+1),
            "Possible Message": msg}
            for i, msg in enumerate(decrypted_messages)]
        st.dataframe(table_data, use_container_width=True, hide_index=True)

add_nav_buttons("Brute_Force_Decryptor")