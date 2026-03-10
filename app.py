import streamlit as st

st.title("Monday.com BI Agent")

st.write("Hello Khushi! Your Streamlit app is working.")

question = st.text_input("Ask a business question")

if question:
    st.write("Analyzing:", question)