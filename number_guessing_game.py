import streamlit as st
import random

def run():
    st.title("🔢 Number Guessing Game")
    st.markdown("Let the computer guess your number!")

    # Initialize session state for low, high, and feedback
    if "low" not in st.session_state:
        st.session_state.low = 1
    if "high" not in st.session_state:
        st.session_state.high = 100
    if "feedback" not in st.session_state:
        st.session_state.feedback = ''

    # Instructions
    st.write("Think of a number between 1 and 100.")
    st.write("The computer will try to guess your number. Tell it if the guess is too high (H), too low (L), or correct (C).")

    # Computer's guess
    comp_guess = (st.session_state.low + st.session_state.high) // 2
    feedback = st.text_input(f"Is {comp_guess} too high (H), too low (L), or correct (C)? ").lower()

    # Process feedback
    if feedback == 'h':
        st.session_state.high = comp_guess - 1
        st.write(f"The computer will now guess between {st.session_state.low} and {st.session_state.high}.")
    elif feedback == 'l':
        st.session_state.low = comp_guess + 1
        st.write(f"The computer will now guess between {st.session_state.low} and {st.session_state.high}.")
    elif feedback == 'c':
        st.success(f"Yay! The computer guessed your number, {comp_guess}, correctly!")
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.feedback = ''
    elif feedback:
        st.error("Invalid input! Please enter 'H', 'L', or 'C'.")

    # Reset button
    if st.button("Reset Game"):
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.feedback = ''
        st.success("Game reset! Think of a new number.")