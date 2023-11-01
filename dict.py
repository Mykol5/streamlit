import streamlit as st
import random

# Vocabulary data (you can replace this with your own vocabulary)
vocabulary = {
    "apple": "manzana",
    "banana": "plátano",
    "car": "coche",
    "house": "casa",
    "dog": "perro",
}

# Create a Streamlit web app
st.title("Language Learning App")

# Quiz function
def vocabulary_quiz(vocabulary):
    score = 0
    total_questions = len(vocabulary)
    question_order = list(vocabulary.keys())
    random.shuffle(question_order)

    for word in question_order:
        st.write(f"What is the Spanish word for '{word}'?")
        user_answer = st.text_input(f"Your answer for '{word}':")

        if user_answer.lower() == vocabulary[word].lower():
            st.write("Correct!")
            score += 1
        else:
            st.write(f"Sorry, the correct answer is '{vocabulary[word]}'.")

    st.write(f"You got {score} out of {total_questions} correct.")

# Start the quiz
if st.button("Start Vocabulary Quiz"):
    vocabulary_quiz(vocabulary)

# Pronunciation exercise (you can add pronunciation exercises using additional libraries or services)
st.header("Pronunciation Exercise")
st.write("You can add pronunciation exercises using audio samples or text-to-speech libraries.")
st.write("Practice saying the words out loud for better pronunciation.")

# Vocabulary list
st.header("Vocabulary List")
st.write("Here are some vocabulary words you can learn:")
for word, translation in vocabulary.items():
    st.write(f"- {word} ({translation})")
