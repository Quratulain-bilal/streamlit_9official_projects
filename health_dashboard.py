import streamlit as st

def run():
    st.title("🩺 Health Dashboard")
    st.markdown("Track your daily health metrics!")

    # Calorie Tracker
    st.subheader("Calorie Tracker 🍎")
    calorie_goal = st.number_input("Enter your daily calorie goal:", min_value=500, max_value=5000, value=2000)
    calories_consumed = st.number_input("Enter calories consumed today:", min_value=0, max_value=10000, value=0)
    calories_remaining = calorie_goal - calories_consumed

    if calories_remaining > 0:
        st.success(f"You have {calories_remaining} calories remaining today!")
    else:
        st.error("You have exceeded your calorie goal today! ⚠️")

    # Hydration Reminder
    st.subheader("Hydration Reminder 💧")
    water_goal_liters = st.slider("Set your daily water goal (in liters):", min_value=1, max_value=5, value=2)
    water_goal_liters = float(water_goal_liters)  # Convert to float
    water_consumed_liters = st.number_input(
        "How much water have you consumed today? (in liters):",
        min_value=0.0,
        max_value=water_goal_liters,
        value=0.0,
        format="%.1f"
    )
    
    if water_consumed_liters >= water_goal_liters:
        st.success("Great job! You've met your hydration goal! ✅")
    else:
        st.warning(f"Drink {water_goal_liters - water_consumed_liters:.1f} more liters of water today!")

    # Daily Step Goal
    st.subheader("Daily Step Goal 🚶‍♂️")
    step_goal = st.number_input("Enter your daily step goal:", min_value=1000, max_value=20000, value=10000)
    steps_taken = st.number_input("How many steps have you taken today?", min_value=0, max_value=step_goal * 2, value=0)
    
    if steps_taken >= step_goal:
        st.success("Congratulations! You've reached your step goal! 🎉")
    else:
        st.info(f"You need {step_goal - steps_taken} more steps to reach your goal.")