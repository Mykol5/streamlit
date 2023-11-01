import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the web app
st.title("Sine and Cosine Plot")

# Add a slider to let the user choose the frequency
frequency = st.slider("Select Frequency (in Hertz):", 1, 10, 5)

# Create a time vector
t = np.linspace(0, 2 * np.pi, 1000)

# Create the sine and cosine waves based on user input
sine_wave = np.sin(2 * np.pi * frequency * t)
cosine_wave = np.cos(2 * np.pi * frequency * t)

# Create a plot using Matplotlib
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, sine_wave, label="Sine")
ax.plot(t, cosine_wave, label="Cosine")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title(f"Sine and Cosine Waves (Frequency: {frequency} Hz)")
ax.legend()

# Display the plot using st.pyplot
st.pyplot(fig)
