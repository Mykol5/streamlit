import streamlit as st

# Create a Streamlit web app
st.title("User Dashboard and Game")

# Define a dictionary for user authentication (for demonstration purposes)
user_credentials = {
    "username": "password",
    "demo_user": "demo_password"
}

# Sidebar for user login
st.sidebar.header("User Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Check if the user is authenticated
if st.sidebar.button("Login"):
    if username in user_credentials and password == user_credentials[username]:
        st.success(f"Welcome, {username}!")
        st.write("## Play a Simple Game")
        st.write("Here's a simple game for you to play!")

        # Add your game code here or use a game library

if not st.sidebar.button("Logout"):  # Use a unique key for the button
    st.write("## Welcome to the Dashboard")
    st.write("Please log in to access the game.")
