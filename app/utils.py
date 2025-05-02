import streamlit as st
def apply_btn_styles():
    button_style = """
        <style>
        div.stButton > button:first-child {
            background-color: #000;
            color: white;
            height: 3em;
            width: auto;
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

# maybe will use it later
def add_back_button():
    if st.button("""⬅  Back to Home"""):
        st.switch_page("streamlit_app.py")

def add_nav_buttons(current_page_name):
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    if col1.button("""⬅  Back to Home"""):
        st.switch_page("streamlit_app.py")
    if current_page_name == "Encryptor":
        if col2.button("Decrypt by Brute Force") and current_page_name != "Brute_Force_Decryptor":
            st.switch_page("pages/2_Brute_Force_Decryptor.py")
        if col3.button("Auto-decrypt a Message") and current_page_name != "Auto_Decryptor":
            st.switch_page("pages/3_Auto_Decryptor.py")
    
    elif current_page_name == "Brute_Force_Decryptor":
        if col2.button("Encrypt a Message") and current_page_name != "Encryptor":
            st.switch_page("pages/1_Encryptor.py")
        if col3.button("Auto-decrypt a Message") and current_page_name != "Auto_Decryptor":
            st.switch_page("pages/3_Auto_Decryptor.py")
    
    elif current_page_name == "Auto_Decryptor":
        if col2.button("Encrypt a Message") and current_page_name != "Encryptor":
            st.switch_page("pages/1_Encryptor.py")
        if col3.button("Decrypt by Brute Force") and current_page_name != "Brute_Force_Decryptor":
            st.switch_page("pages/2_Brute_Force_Decryptor.py")
    