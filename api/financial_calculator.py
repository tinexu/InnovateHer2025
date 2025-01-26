import streamlit as st

def calculate_future_value(initial_investment, monthly_contribution, annual_rate, years):
    """
    Calculate the future value of an investment with monthly contributions.
    """
    monthly_rate = annual_rate / 12 / 100  # Convert annual rate to monthly rate
    months = years * 12  # Total number of months
    future_value = initial_investment * (1 + monthly_rate) ** months

    for month in range(1, months + 1):
        future_value += monthly_contribution * (1 + monthly_rate) ** (months - month)

    return future_value

# Streamlit app
st.title("Financial Planning Calculator")
st.write("Plan your financial goals and calculate future investment value!")

# Input fields
initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, value=1000.0, step=100.0)
monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0.0, value=200.0, step=50.0)
annual_rate = st.number_input("Expected Annual Return (%)", min_value=0.0, value=5.0, step=0.1)
years = st.number_input("Investment Duration (Years)", min_value=1, value=10, step=1)

# Calculate future value
if st.button("Calculate Future Value"):
    future_value = calculate_future_value(initial_investment, monthly_contribution, annual_rate, years)
    st.success(f"The future value of your investment is: ${future_value:,.2f}")

# Additional visualization
import matplotlib.pyplot as plt

if st.button("Show Investment Growth Chart"):
    months = years * 12
    monthly_rate = annual_rate / 12 / 100
    balance = []
    total_contribution = []

    for month in range(1, months + 1):
        total_contributed = initial_investment + monthly_contribution * month
        value = initial_investment * (1 + monthly_rate) ** month
        for m in range(1, month + 1):
            value += monthly_contribution * (1 + monthly_rate) ** (month - m)
        balance.append(value)
        total_contribution.append(total_contributed)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, months + 1), balance, label="Future Value")
    plt.plot(range(1, months + 1), total_contribution, label="Total Contributions")
    plt.xlabel("Months")
    plt.ylabel("Value ($)")
    plt.title("Investment Growth Over Time")
    plt.legend()
    st.pyplot(plt)
