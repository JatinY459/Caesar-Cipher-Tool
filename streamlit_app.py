import streamlit as st
from app.cipher import *
from app.app_config import apply_page_config

# page configuration
apply_page_config()

st.title("Caesar Cipher Playground 🔏")
st.markdown("##### This app allows you to encrypt and decrypt messages using the Caesar cipher.")

with st.container():
    st.markdown("""
                <style>
                    .container {
                        background-color: rgb(30, 30, 30);
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
                        margin: 1.25rem 0;
                    }
                </style>
                <div class='container'>
                <div style='font-size: 1.5rem; font-weight: 700;'>
                    What is the Caesar cipher?
                </div>
                <div style='font-size: 1.2rem' >
                    The Caesar Cipher is one of the oldest known encryption techniques. It was used by Julius Caesar himself, in the Caesar cipher the letters are shifted by a constant number to create unreadable messages. This tool lets you explore Caesar-style encryption, test brute-force approach on encrypted messages, and auto-decrypt ciphers using common English words.
                </div>
                </div>""", unsafe_allow_html=True)


st.markdown("""<div style='font-size: 1.2rem; font-weight: 600; margin-top:1rem; margin-bottom:2rem;'>What would you like to do next? Choose an option below.</div>""", unsafe_allow_html=True)

button_style = """
<style>
div.stButton > button:first-child {
    background-color: #000;
    color: white;
    height: 3em;
    width: 70%;
    border-radius: 10px;
    border: 2px solid rgb(30,30,30);
    font-size: 1rem;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:first-child:hover {
    background-color: rgb(30,30,30);
    font-weight: 900;
    transform: scale(1.02);
}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

col1, col2 = st.columns(2)
if col1.button("Encrypt a Message"):
    st.switch_page("pages/1_Encryptor.py")
elif col2.button("Decrypt by Brute Force"):
    st.switch_page("pages/2_Brute_Force_Decryptor.py")
elif col1.button("Auto-decrypt a Message"):
    st.switch_page("pages/3_Auto_Decryptor.py")
elif col2.button("About the App"):
    st.switch_page("pages/4_About.py")  

st.markdown("---")

st.markdown("<div style='text-align: center; font-weight:800; font-size: 1.5rem;'>Made with ❤️ by Jatin Yadav.</div>", unsafe_allow_html=True)
st.markdown("""
            <style>
                .my-btn {
                    background-color: #000;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 10px;
                    border: 2px solid rgb(30,30,30);
                    text-decoration: none;
                    font-size: 1rem;
                    font-weight: bold;
                    transition: 0.3s;
                    margin: 0 1rem;
                }
                .my-btn:hover {
                    background-color: rgb(30,30,30);
                    font-weight: 900;
                    transform: scale(1.02);
                }
            </style>
            <div style='text-align: center; margin-top: 2rem;'>
                <a href='https://github.com/JatinY459/' class='my-btn' target='_blank'>GitHub</a>
                <a href='https://www.linkedin.com/in/jatinyadav459/' class='my-btn' target='_blank'>LinkedIn</a>
                <a href='https://github.com/JatinY459/blob/main/README.md' class='my-btn' target='_blank'>Project Info</a>
            </div>""", unsafe_allow_html=True)
st.markdown("---")