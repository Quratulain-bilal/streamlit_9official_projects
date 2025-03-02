import streamlit as st
import random

def run():
    st.title("✊ Rock-Paper-Scissors Game ✌️")
    st.markdown("Play against the computer and see who wins!")

    # Define choices
    choices = ["Rock", "Paper", "Scissors"]

    # User input
    st.subheader("Choose your move:")
    user_choice = st.selectbox("Select one:", choices)

    # Computer's choice
    computer_choice = random.choice(choices)

    # Play button
    if st.button("Play"):
        st.write(f"Your choice: **{user_choice}**")
        st.write(f"Computer's choice: **{computer_choice}**")

        # Determine the winner
        if user_choice == computer_choice:
            st.info("It's a tie! 🤝")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            st.success("You win! 🎉")
        else:
            st.error("You lose! 😢")