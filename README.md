# 📄 Caesar Cipher Tool

A simple cipher tool to **encrypt**, **brute-force decrypt**, and **auto-decrypt** Caesar cipher messages — all wrapped in a clean Streamlit interface.

## 🚀 Features

- 🔐 **Encrypt a message** using Caesar cipher with a user-defined shift.
- 🔎 **Brute-force decrypt** a ciphered message by generating all 25 possible shifts.
- 🧠 **Auto-decrypt** intelligently guesses the correct message using a list of 3000 common English words .
- 🖥️ Clean, minimal **multi-page Streamlit UI**.
- 🌐 Hosted online and open-source!

## 🧠 What is Caesar Cipher?

The Caesar Cipher is a classical encryption technique where each letter in the plaintext is shifted by a fixed number of positions. For example, with a shift of 3:

- `HELLO` → `KHOOR`

## 📂 Project Structure

```
caesar-cipher-tool/
│
├── app/
│   ├── cipher.py          # Encryption and decryption logic
│   ├── decryptor.py       # Brute-force functionality
│   ├── utils.py           # Helper functions (e.g., sanitization)
│
├── pages/
│   ├── 1_Encrypt.py
│   ├── 2_Brute_Force_Decrypt.py
│   ├── 3_Auto_Decrypt.py
│
├── static/                # Assets like images or icons
│
├── streamlit_app.py       # Main entry point
├── requirements.txt       # Dependencies
├── README.md              # You’re reading it!
├── .gitignore
└── test.py                # used for testing the file
```

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/jatinyadav01/caesar-cipher-tool.git
cd caesar-cipher-tool

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

## 🌍 Live Demo

👉 [Try it on Streamlit Cloud](https://cipher-playground.streamlit.app/)

## 📚 Tech Stack

- **Python**
- **Streamlit**
- **Custom Caesar Cipher logic**

## 📎 Credits

A simple cipher tool. Developed by **Jatin Yadav**.  
[GitHub](https://github.com/jatinyadav01) · [LinkedIn](https://linkedin.com/in/jatinyadav01)
