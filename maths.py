import streamlit as st
import random

# Function to generate a math question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Ensure division results in an integer
        num1, num2 = num1 * num2, num2
        answer = num1 / num2
    
    return f"What is {num1} {operator} {num2}?", answer

# Create a Streamlit web app
st.title("Math Quiz Game")

# Initialize the game
score = 0

# Display a button to start the game
start_game = st.button("Start Game")
if start_game:
    st.write("Let's play the Math Quiz Game!")

# Main game loop
if start_game:
    # Generate the first question
    question, correct_answer = generate_question()
    
    # Display the question and collect user input
    user_answer = st.number_input(question)
    
    if st.button("Check Answer"):
        if user_answer == correct_answer:
            st.write("Correct! Well done.")
            score += 1
        else:
            st.write(f"Oops! The correct answer is {correct_answer}.")

    # Display the current score
    st.write(f"Your current score: {score}")

    # Display a button to generate the next question
    next_question = st.button("Next Question")
    if next_question:
        # Generate the next question
        question, correct_answer = generate_question()

