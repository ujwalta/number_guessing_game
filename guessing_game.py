import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game", page_icon="🎮")
st.title("🎮 Guess the Number Game!")
st.write("I am thinking of a number between 1 and 50. Can you guess it?")

# Initialize session state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 50)
if "attempts" not in st.session_state:
    st.session_state.attempts = 7
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.number_to_guess = random.randint(1, 50)
    st.session_state.attempts = 7
    st.session_state.game_over = False
    st.success("Game restarted! Try guessing a new number.")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

    if st.button("Submit Guess"):
        if guess == st.session_state.number_to_guess:
            st.balloons()
            st.success(f"🎉 Wow! You guessed it right! The number was {st.session_state.number_to_guess}.")
            st.session_state.game_over = True
        else:
            st.session_state.attempts -= 1
            if st.session_state.attempts == 0:
                st.error(f"💀 Game Over! The number was {st.session_state.number_to_guess}.")
                st.session_state.game_over = True
            elif guess < st.session_state.number_to_guess:
                st.warning(f"🔼 Too low! Attempts left: {st.session_state.attempts}")
            else:
                st.warning(f"🔽 Too high! Attempts left: {st.session_state.attempts}")
