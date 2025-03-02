
import streamlit as st

def run():
    st.title("📝 Sir's Form Submission")
    st.markdown("Fill out the form below to submit your details.")

    # Add Google Form link
    st.markdown("Click the link below to submit your details:")
    st.markdown("[Submit Here](https://forms.gle/CixPAnwR726zuosK6)")

    # Optional: Add a text input for feedback
    feedback = st.text_area("Any additional feedback?")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.error("Please enter some feedback before submitting.")
