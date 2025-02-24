import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("My first Streamlit App")
st.write("This is to do cllas activity 24")

user_input = st.text_input("Enter name")
st.write('Your name is' ,user_input)

st.write("You are", st.slider("What is your age", 1, 100), "years old")

if st.button('Say hello'):
    st.write("Hello there")


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [24, 30, 35, 40, 29]
}
df = pd.DataFrame(data)

st.write("Here is the DataFrame:")
st.dataframe(df)

fig, ax = plt.subplots()
ax.hist(df["Age"], bins=5, color='blue', alpha=0.7)
ax.set_title("Histogram of Ages")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")

# Display the plot in Streamlit
st.pyplot(fig)

# 6. Advanced Layouts
col1, col2 = st.columns(2)

with col1:
    st.write("Hello")

with col2:
    st.write("World")

# Expander for additional information
with st.expander("More Information"):
    st.write("This is a sample Streamlit application")
