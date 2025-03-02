import streamlit as st
import random

def run():
    st.title("🎮 Hangman Game")
    st.markdown("Guess the hidden word one letter at a time!")

    # Initialize session state variables
    if "word" not in st.session_state:
        words = ["PYTHON", "STREAMLIT", "PROJECT", "CODING", "GAME"]
        st.session_state.word = random.choice(words)
        st.session_state.guessed_letters = set()
        st.session_state.lives = 6

    word = st.session_state.word
    guessed_letters = st.session_state.guessed_letters
    lives = st.session_state.lives

    # Display the current state of the word
    display_word = " ".join([letter if letter in guessed_letters else "-" for letter in word])
    st.subheader(f"Word: {display_word}")
    st.write(f"Lives left: {lives} ❤️")

    # Add a unique key using session state
    guess_key = "hangman_guess"
    guess = st.text_input("Guess a letter:", max_chars=1, key=guess_key).upper()

    if guess:
        if guess in guessed_letters:
            st.warning("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            st.success(f"Good job! `{guess}` is in the word.")
        else:
            lives -= 1
            st.error(f"Oops! `{guess}` is not in the word.")

        # Update session state
        st.session_state.guessed_letters = guessed_letters
        st.session_state.lives = lives

    # Check if the game is won or lost
    if set(word).issubset(guessed_letters):
        st.balloons()
        st.success(f"Congratulations! You guessed the word: `{word}`")
        reset_game()
    elif lives == 0:
        st.error(f"Game Over! The word was: `{word}`")
        reset_game()

def reset_game():
    """Reset the game state."""
    st.session_state.word = None
    st.session_state.guessed_letters = None
    st.session_state.lives = None