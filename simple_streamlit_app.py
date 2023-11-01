# Import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Create a Streamlit web app
st.title("Simple Streamlit Web App")

# Add a sidebar with user input
st.sidebar.header("User Input")
user_input = st.sidebar.slider("Select a number:", 1, 10, 5)

# Generate some data based on user input
data = pd.DataFrame({
    'x': np.arange(user_input),
    'y': np.arange(user_input) ** 2
})

# Display the data table
st.write("Data Table:")
st.write(data)

# Create a scatter plot using Altair
st.write("Scatter Plot:")
scatter_chart = alt.Chart(data).mark_circle().encode(
    x='x',
    y='y'
).properties(
    width=400,
    height=400
)
st.altair_chart(scatter_chart)
