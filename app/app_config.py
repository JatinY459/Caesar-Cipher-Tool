import streamlit as st
def apply_page_config():
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

