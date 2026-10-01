import streamlit as st

st.title("Imad Bhai ka Result App")

marks = st.number_input("Apne marks likho:", 0, 100)

if st.button("Result Dekho"):
    if marks >= 50:
        st.success("Mubarak ho, ap PASS ho!")
    else:
        st.error("Koshish jari rakho, ap FAIL ho.")