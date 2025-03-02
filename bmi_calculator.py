import streamlit as st

def run():
    st.title("📊 BMI Calculator")
    st.markdown("Enter your weight and height to calculate your Body Mass Index (BMI).")

    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Enter your weight in kilograms:", min_value=1.0, format="%.2f")
    with col2:
        height = st.number_input("Enter your height in centimeters:", min_value=10.0, format="%.2f")

    if weight > 0 and height > 0:
        height_in_m = height / 100
        bmi = weight / (height_in_m ** 2)
        st.subheader(f"Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.error("You are underweight! ⚠️")
        elif 18.5 <= bmi < 24.9:
            st.success("You are normal weight! ✅")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight! ⚠️")
        else:
            st.error("You are obese! ⚠️")