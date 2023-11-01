import streamlit as st
import sqlite3
import random

# Create a Streamlit web app
st.title("User Dashboard and Game")

# Connect to the SQLite database
conn = sqlite3.connect("user_database.db")
cursor = conn.cursor()

# Create a table for users if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")
conn.commit()

# Function to add a new user
def add_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

# Function to check if a user exists
def user_exists(username, password):
    cursor.execute("SELECT username, password FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone() is not None

# Function to check if a username is available
def is_username_available(username):
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    return cursor.fetchone() is None

# Registration
st.sidebar.header("User Registration")
new_username = st.sidebar.text_input("New Username")
new_password = st.sidebar.text_input("New Password", type="password")
if st.sidebar.button("Create Account"):
    if new_username and new_password and is_username_available(new_username):
        add_user(new_username, new_password)
        st.sidebar.success("Account created. Please log in.")
    elif not new_username or not new_password:
        st.sidebar.error("Both username and password are required.")
    else:
        st.sidebar.error("Username already exists. Try a different one.")

# Log in
st.sidebar.header("User Login")
login_username = st.sidebar.text_input("Username")
login_password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button("Sign In"):
    if login_username and login_password:
        if user_exists(login_username, login_password):
            st.sidebar.success(f"Welcome, {login_username}!")

            # Rock, Paper, Scissors Game
            st.write("## Rock, Paper, Scissors Game")
            st.write("Let's play a game of Rock, Paper, Scissors!")

            play_again = True

            while play_again:
                user_choice = st.selectbox("Select your move:", ("Rock", "Paper", "Scissors"))
                computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                st.write(f"Your choice: {user_choice}")
                st.write(f"Computer's choice: {computer_choice}")

                if user_choice == computer_choice:
                    st.write("It's a tie!")
                elif (
                    (user_choice == "Rock" and computer_choice == "Scissors")
                    or (user_choice == "Paper" and computer_choice == "Rock")
                    or (user_choice == "Scissors" and computer_choice == "Paper")
                ):
                    st.success("You win!")
                else:
                    st.error("Computer wins!")

                play_again = st.button("Play Again")

        else:
            st.sidebar.error("Authentication failed. Please check your username and password.")
    else:
        st.sidebar.error("Both username and password are required.")

# Close the database connection
conn.close()
