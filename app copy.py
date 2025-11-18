import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Trivia Quiz",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Trivia Quiz")
st.write("App deployed successfully!")

# Test if imports work
df = pd.DataFrame({"test": [1, 2, 3]})
st.write(df)
