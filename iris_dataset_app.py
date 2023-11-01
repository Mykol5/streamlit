import streamlit as st
import pandas as pd
import seaborn as sns

# Set the title of the web app
st.title("Iris Dataset Exploration")

# Load the Iris dataset
@st.cache  # Cache the data for improved performance
def load_data():
    data = sns.load_dataset("iris")
    return data

iris_data = load_data()

# Display the dataset
st.write("### Iris Dataset")
st.write(iris_data)

# Sidebar for user options
species = st.sidebar.selectbox("Select a species:", iris_data["species"].unique())
filtered_data = iris_data[iris_data["species"] == species]

# Display a summary of the selected species
st.write(f"### Summary for {species} Species")
st.write(filtered_data.describe())

# Create a pair plot to visualize relationships between features
st.write("### Pair Plot")
sns.pairplot(filtered_data, hue="species")
st.pyplot()
