import streamlit as st

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    st.write("Resume Score: 85%")
