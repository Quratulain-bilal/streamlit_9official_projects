import streamlit as st
import random
import string

def run():
    st.title("🔒 Password Generator")
    st.markdown("Generate a strong and secure password.")

    length = st.slider("Select password length:", min_value=6, max_value=20, value=12)
    include_numbers = st.checkbox("Include numbers")
    include_symbols = st.checkbox("Include symbols")

    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%&*.?"

    if st.button("Generate Password"):
        password = "".join(random.choices(chars, k=length))
        st.subheader(f"Your password is: `{password}`")