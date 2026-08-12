import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🎯 Quiz App")

response = requests.get(f"{API_URL}/questions")

if response.status_code == 200:

    questions = response.json()

    score = 0

    for question in questions:

        st.subheader(question["question"])

        answer = st.radio(
            "Choose your answer:",
            question["options"],
            key=question["id"]
        )

        if st.button(
            "Check Answer",
            key=f"button_{question['id']}"
        ):

            if answer == question["answer"]:
                st.success("Correct! 🎉")
            else:
                st.error("Wrong answer ❌")

else:
    st.error("Cannot connect to FastAPI")