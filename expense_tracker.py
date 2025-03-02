import streamlit as st

def run():
    st.title("💸 Expense Tracker")
    st.markdown("Track your daily expenses and stay within your budget!")

    # Input expenses
    st.subheader("Add an Expense")
    expense_name = st.text_input("Expense Name:")
    expense_amount = st.number_input("Expense Amount ($):", min_value=0.0, format="%.2f")
    add_expense = st.button("Add Expense")

    # Store expenses in session state
    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    if add_expense and expense_name and expense_amount > 0:
        st.session_state.expenses.append({"name": expense_name, "amount": expense_amount})
        st.success(f"Added expense: {expense_name} (${expense_amount:.2f})")

    # Display expenses
    st.subheader("Your Expenses")
    if st.session_state.expenses:
        total_expenses = sum(expense["amount"] for expense in st.session_state.expenses)
        st.write("### Expense List:")
        for expense in st.session_state.expenses:
            st.write(f"- {expense['name']}: ${expense['amount']:.2f}")
        st.write(f"### Total Expenses: ${total_expenses:.2f}")
    else:
        st.info("No expenses added yet.")