import streamlit as st

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # In a real-world application, you would perform authentication here
        if username == "admin" and password == "admin":
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

def main():
    st.title("Login Page")
    login()

if __name__ == "__main__":
    main()
